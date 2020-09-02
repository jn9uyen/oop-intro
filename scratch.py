class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

    def toDashDate2(self, date):
        return date.replace("/", "-")


class DatesWithSlashes(Dates):
    def getDate(self):
        return self.toDashDate(self.date)

    def getDate2(self):
        return Dates.toDashDate(self.date)


date = Dates("15-12-2016")
dateFromDB = DatesWithSlashes("15/12/2016")

dateFromDB.getDate()
dateFromDB.getDate2()

if(date.getDate() == dateFromDB.getDate()):
    print("Equal")
else:
    print("Unequal")


def predict(self, data):
    data['crn'] = data['crn'].values.astype('str')

    scored = (
        data[data['template_id'] == 'base'][
            ['crn', 'template_id', 'l8w_spd']
        ]
        .drop_duplicates()
        .copy()
    )
    assert scored.shape[0] == data.shape[0]
    cols_id = ['crn', 'template_id']

    campaign_type = self.get_campaign_type()

    # Base spend models
    remote_spd_model = MMMConfig.MODEL_PATH[campaign_type]['spd']
    local_spd_model = Path(remote_spd_model).name
    gcw.cp(inputLocation=remote_spd_model, outputLocation="./").run()
    mdl_spd = self.load_model(local_spd_model)

    LOG.info('process base')
    filtered_data = data[
        (data['model_type'] == 'spd') & (data['camp_rdm_flag'] == 0)
    ].copy()
    tmp = self.load_prep_data(
        filtered_data, mdl_spd, filtered_data[cols_id], 'base_spd'
    )
    scored = scored.merge(tmp, on=cols_id, how='left')

    cols = [
        'crn',
        'base_spd',
        'l8w_spd',
    ]
    return scored[cols]




def predict(self, data):

    # if offer is not model supported
    if data[data['random_allocation'] == True].shape[0] > 0:  # NOQA
        LOG.info(f'Empty prediction')
        return self.empty_prediction(data)

    data = self.columns_rename(data)

    data['crn'] = data['crn'].values.astype('str')

    scored = (
        data[data['template_id'] != 'base'][self.get_score_col()]
        .drop_duplicates()
        .copy()
    )
    cols_id = self.get_cols_id()
    campaign_type = self.get_campaign_type()

    # Redemption model
    remote_rdm_model = MMMConfig.MODEL_PATH[campaign_type]['rdm']
    local_rdm_model = Path(remote_rdm_model).name
    gcw.cp(inputLocation=remote_rdm_model, outputLocation="./").run()
    mdl_rdm = self.load_model(local_rdm_model)

    filtered_data = data[data['model_type'] == 'rdm'].copy()
    LOG.info('process rdm')
    tmp = self.load_prep_data(
        filtered_data, mdl_rdm, filtered_data[cols_id], 'p_rdm'
    )
    scored = scored.merge(tmp, on=cols_id, how='left')

    # Spend model
    remote_spd_model = MMMConfig.MODEL_PATH[campaign_type]['spd']
    local_spd_model = Path(remote_spd_model).name
    gcw.cp(inputLocation=remote_spd_model, outputLocation="./").run()
    mdl_spd = self.load_model(local_spd_model)
    # Spend models - spd|rdm
    LOG.info('process spd|rdm')
    filtered_data = data[
        (data['model_type'] == 'spd') & (data['camp_rdm_flag'] == 1)
    ].copy()
    tmp = self.load_prep_data(
        filtered_data, mdl_spd, filtered_data[cols_id], 'spd|rdm'
    )
    scored = scored.merge(tmp, on=cols_id, how='left')
    # Spend models - spd|not_rdm
    LOG.info('process spd|not_rdm')
    filtered_data = data[
        (data['model_type'] == 'spd') & (data['camp_rdm_flag'] == 0)
    ].copy()
    tmp = self.load_prep_data(
        filtered_data, mdl_spd, filtered_data[cols_id], 'spd|not_rdm'
    )
    scored = scored.merge(tmp, on=cols_id, how='left')

    # # Base models
    # LOG.info('process base')
    # remote_base_spd_model = MMMConfig.MODEL_PATH['base']['spd']
    # local_spd_model = Path(remote_base_spd_model).name
    # gcw.cp(inputLocation=remote_base_spd_model, outputLocation="./").run()
    # mdl_spd = self.load_model(local_spd_model)

    # filtered_data = data[
    #     (data['model_type'] == 'spd') & (data['Template_id'] == 'base')
    # ].copy()

    # tmp = self.load_prep_data(
    #     filtered_data, mdl_spd, data[cols_id], 'base_spd'
    # )
    # scored = scored.merge(tmp, on=cols_id, how='left')

    # -------------------------------------------------
    # Post-score
    # -------------------------------------------------

    scored.rename(
        columns={'f0_campaign_type': 'offer_type', 'f0_reward': 'reward',},
        inplace=True,
    )
    scored['reward'] = self.get_reward(scored)
    # df['reward'] = df['reward'].values.astype('float32')
    # df['reward'] = df['reward'].fillna(0)
    # df['camp_dur_wks'] = df['camp_dur_wks'].values.astype('float32') #uint8

    cols = self.get_cols()
    return scored[cols]