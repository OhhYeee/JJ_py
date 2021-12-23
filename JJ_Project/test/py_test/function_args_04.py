dict1 = {}
dict2 = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
list01 = ['a', 'b', 'c', 'd']


# list02 = []


def add_feature(dict_1, dict_2, *feature):
    for i in feature:
        dict_1[i] = dict_2[i]


add_feature(dict1, dict2, *list01)
print(dict1)


# add_feature(dict1, dict2, *list02)
# print(dict1)


def add_feature(feature_dict, feature_result, feature_list):
    for feature in feature_list:
        feature_dict[feature] = feature_result[feature]


feature_dict = {}
feature_result = {"bhv_screen_merge_distinct_cnt_borrow_step1_date": 0,
                  "bhv_screen_merge_distinct_cnt_homepage_date": 0,
                  "bhv_screen_merge_last_work_info_duration": None,
                  "bhv_screen_merge_sum_borrow_step1_duration": None,
                  "bhv_screen_merge_sum_borrow_step2_duration": None,
                  "bhv_screen_merge_sum_borrow_step3_duration": None,
                  "bhv_screen_merge_sum_consumer_finance_step4_duration": None,
                  "bhv_screen_merge_sum_duration": None,
                  "bhv_screen_merge_sum_duration_last2day": None,
                  "bhv_screen_merge_sum_login_via_password_duration": None,
                  "bhv_screen_merge_sum_login_via_password_duration_last1day": None,
                  "bhv_screen_merge_sum_me_duration": None,
                  "bhv_screen_merge_sum_me_duration_night": None,
                  "bhv_screen_merge_sum_work_info_duration_1daybefore": None,
                  "bhv_screen_merge_sum_borrow_step1_duration_last2day": None}

feature_list = ['bhv_screen_merge_distinct_cnt_borrow_step1_date',
                'bhv_screen_merge_distinct_cnt_homepage_date',
                'bhv_screen_merge_last_work_info_duration',
                'bhv_screen_merge_sum_borrow_step1_duration',
                'bhv_screen_merge_sum_borrow_step2_duration',
                'bhv_screen_merge_sum_borrow_step3_duration',
                'bhv_screen_merge_sum_consumer_finance_step4_duration',
                'bhv_screen_merge_sum_duration',
                'bhv_screen_merge_sum_duration_last2day',
                'bhv_screen_merge_sum_login_via_password_duration',
                'bhv_screen_merge_sum_login_via_password_duration_last1day',
                'bhv_screen_merge_sum_me_duration',
                'bhv_screen_merge_sum_me_duration_night',
                'bhv_screen_merge_sum_work_info_duration_1daybefore',
                'bhv_screen_merge_sum_borrow_step1_duration_last2day']

add_feature(feature_dict, feature_result, feature_list)



print(feature_dict)
