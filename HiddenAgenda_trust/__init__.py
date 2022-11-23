from otree.api import *
import random

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'hiddenagenda_decisions'
    players_per_group = None
    num_rounds = 1 # 2 needed for attention check questions

    fixed_pay = cu(5)
    avg_pay = cu(10)

    num_attention_checks = 5
    num_final_questions = 10
    num_interaction_formats = 4
    num_evaluations = 10

    # Objective true probabilities
    round_1_prob = 0.1
    round_2_prob = 0.2
    round_3_prob = 0.3
    round_4_prob = 0.4
    round_5_prob = 0.45
    round_6_prob = 0.55
    round_7_prob = 0.65
    round_8_prob = 0.7
    round_9_prop = 0.8
    round_10_prob = 0.9


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Process variables
    starting_time = models.LongStringField(doc="Time at which Informed Consent is given and experiment starts")
    begintrial_time = models.LongStringField(doc="Time at which trial round is started")

    # Response variables for attention checks
    attention_check_1 = models.FloatField(initial=999,
                                          label="Q1: ...?",
                                          doc="Attention check: ...)")
    attention_check_2 = models.FloatField(initial=999,
                                          label="Q2: ...?",
                                          doc="Attention check: ..."
                                              "(1: ... "
                                              " 2: ... "
                                              " 3: ...)"
                                          )
    attention_check_3 = models.FloatField(initial=999,
                                          label="Q3: ...?",
                                          doc="Attention check: ..."
                                              "(1: ... "
                                              " 2: ... "
                                              " 3: ...)"
                                          )
    attention_check_4 = models.FloatField(initial=999,
                                          label="Q4: ...?",
                                          doc="Attention check: ..."
                                              "(1: ... "
                                              " 2: ... "
                                              " 3: ...)"
                                          )
    attention_check_5 = models.FloatField(initial=999,
                                          label="Q5: ...?",
                                          doc="Attention check: ..."
                                              "(1: ... "
                                              " 2: ... "
                                              " 3: ...)"
                                          )
    attention_check_6 = models.FloatField(inital=999,
                                          label="Q6: What does the bonus you can earn by solving the task"
                                                " depend on?",
                                          doc="Attention check: ..."
                                              "(1: ... "
                                              " 2: ... "
                                              " 3: ...)"
                                          )

    failed_attention_check = models.BooleanField(initial=False,
                                                 doc="True if attention check has not been passed at first attempt")

    attention_check_tries = models.IntegerField(initial=1,
                                                doc="Number of attempts needed to pass attention check questions")

    # Response variables for elicitation of trust in estimates
    # For estimates from face-to-face treatment
    ftf_round_1_lower = models.FloatField(doc="Lower bound of confidence interval on round 1. ftf estimate")
    ftf_round_1_upper = models.FloatField(doc="Lower upper of confidence interval on round 1. ftf estimate")
    ftf_round_2_lower = models.FloatField(doc="Lower bound of confidence interval on round 2. ftf estimate")
    ftf_round_2_upper = models.FloatField(doc="Lower upper of confidence interval on round 2. ftf estimate")
    ftf_round_3_lower = models.FloatField(doc="Lower bound of confidence interval on round 3. ftf estimate")
    ftf_round_3_upper = models.FloatField(doc="Lower upper of confidence interval on round 3. ftf estimate")
    ftf_round_4_lower = models.FloatField(doc="Lower bound of confidence interval on round 4. ftf estimate")
    ftf_round_4_upper = models.FloatField(doc="Lower upper of confidence interval on round 4. ftf estimate")
    ftf_round_5_lower = models.FloatField(doc="Lower bound of confidence interval on round 5. ftf estimate")
    ftf_round_5_upper = models.FloatField(doc="Lower upper of confidence interval on round 5. ftf estimate")
    ftf_round_6_lower = models.FloatField(doc="Lower bound of confidence interval on round 6. ftf estimate")
    ftf_round_6_upper = models.FloatField(doc="Lower upper of confidence interval on round 6. ftf estimate")
    ftf_round_7_lower = models.FloatField(doc="Lower bound of confidence interval on round 7. ftf estimate")
    ftf_round_7_upper = models.FloatField(doc="Lower upper of confidence interval on round 7. ftf estimate")
    ftf_round_8_lower = models.FloatField(doc="Lower bound of confidence interval on round 8. ftf estimate")
    ftf_round_8_upper = models.FloatField(doc="Lower upper of confidence interval on round 8. ftf estimate")
    ftf_round_9_lower = models.FloatField(doc="Lower bound of confidence interval on round 9. ftf estimate")
    ftf_round_9_upper = models.FloatField(doc="Lower upper of confidence interval on round 9. ftf estimate")
    ftf_round_10_lower = models.FloatField(doc="Lower bound of confidence interval on round 10. ftf estimate")
    ftf_round_10_upper = models.FloatField(doc="Lower upper of confidence interval on round 10. ftf estimate")


    # For estimates from face-to-face treatment with hidden agendas
    ftfha_round_1_lower = models.FloatField(doc="Lower bound of confidence interval on round 1. ftfha estimate")
    ftfha_round_1_upper = models.FloatField(doc="Lower upper of confidence interval on round 1. ftfha estimate")
    ftfha_round_2_lower = models.FloatField(doc="Lower bound of confidence interval on round 2. ftfha estimate")
    ftfha_round_2_upper = models.FloatField(doc="Lower upper of confidence interval on round 2. ftfha estimate")
    ftfha_round_3_lower = models.FloatField(doc="Lower bound of confidence interval on round 3. ftfha estimate")
    ftfha_round_3_upper = models.FloatField(doc="Lower upper of confidence interval on round 3. ftfha estimate")
    ftfha_round_4_lower = models.FloatField(doc="Lower bound of confidence interval on round 4. ftfha estimate")
    ftfha_round_4_upper = models.FloatField(doc="Lower upper of confidence interval on round 4. ftfha estimate")
    ftfha_round_5_lower = models.FloatField(doc="Lower bound of confidence interval on round 5. ftfha estimate")
    ftfha_round_5_upper = models.FloatField(doc="Lower upper of confidence interval on round 5. ftfha estimate")
    ftfha_round_6_lower = models.FloatField(doc="Lower bound of confidence interval on round 6. ftfha estimate")
    ftfha_round_6_upper = models.FloatField(doc="Lower upper of confidence interval on round 6. ftfha estimate")
    ftfha_round_7_lower = models.FloatField(doc="Lower bound of confidence interval on round 7. ftfha estimate")
    ftfha_round_7_upper = models.FloatField(doc="Lower upper of confidence interval on round 7. ftfha estimate")
    ftfha_round_8_lower = models.FloatField(doc="Lower bound of confidence interval on round 8. ftfha estimate")
    ftfha_round_8_upper = models.FloatField(doc="Lower upper of confidence interval on round 8. ftfha estimate")
    ftfha_round_9_lower = models.FloatField(doc="Lower bound of confidence interval on round 9. ftfha estimate")
    ftfha_round_9_upper = models.FloatField(doc="Lower upper of confidence interval on round 9. ftfha estimate")
    ftfha_round_10_lower = models.FloatField(doc="Lower bound of confidence interval on round 10. ftfha estimate")
    ftfha_round_10_upper = models.FloatField(doc="Lower upper of confidence interval on round 10. ftfha estimate")


    # For estimates from delphi treatment
    delphi_round_1_lower = models.FloatField(doc="Lower bound of confidence interval on round 1. delphi estimate")
    delphi_round_1_upper = models.FloatField(doc="Lower upper of confidence interval on round 1. delphi estimate")
    delphi_round_2_lower = models.FloatField(doc="Lower bound of confidence interval on round 2. delphi estimate")
    delphi_round_2_upper = models.FloatField(doc="Lower upper of confidence interval on round 2. delphi estimate")
    delphi_round_3_lower = models.FloatField(doc="Lower bound of confidence interval on round 3. delphi estimate")
    delphi_round_3_upper = models.FloatField(doc="Lower upper of confidence interval on round 3. delphi estimate")
    delphi_round_4_lower = models.FloatField(doc="Lower bound of confidence interval on round 4. delphi estimate")
    delphi_round_4_upper = models.FloatField(doc="Lower upper of confidence interval on round 4. delphi estimate")
    delphi_round_5_lower = models.FloatField(doc="Lower bound of confidence interval on round 5. delphi estimate")
    delphi_round_5_upper = models.FloatField(doc="Lower upper of confidence interval on round 5. delphi estimate")
    delphi_round_6_lower = models.FloatField(doc="Lower bound of confidence interval on round 6. delphi estimate")
    delphi_round_6_upper = models.FloatField(doc="Lower upper of confidence interval on round 6. delphi estimate")
    delphi_round_7_lower = models.FloatField(doc="Lower bound of confidence interval on round 7. delphi estimate")
    delphi_round_7_upper = models.FloatField(doc="Lower upper of confidence interval on round 7. delphi estimate")
    delphi_round_8_lower = models.FloatField(doc="Lower bound of confidence interval on round 8. delphi estimate")
    delphi_round_8_upper = models.FloatField(doc="Lower upper of confidence interval on round 8. delphi estimate")
    delphi_round_9_lower = models.FloatField(doc="Lower bound of confidence interval on round 9. delphi estimate")
    delphi_round_9_upper = models.FloatField(doc="Lower upper of confidence interval on round 9. delphi estimate")
    delphi_round_10_lower = models.FloatField(doc="Lower bound of confidence interval on round 10. delphi estimate")
    delphi_round_10_upper = models.FloatField(doc="Lower upper of confidence interval on round 10. delphi estimate")

    # For estimates from delphi treatment with hidden agendas
    delphiha_round_1_lower = models.FloatField(doc="Lower bound of confidence interval on round 1. delphiha estimate")
    delphiha_round_1_upper = models.FloatField(doc="Lower upper of confidence interval on round 1. delphiha estimate")
    delphiha_round_2_lower = models.FloatField(doc="Lower bound of confidence interval on round 2. delphiha estimate")
    delphiha_round_2_upper = models.FloatField(doc="Lower upper of confidence interval on round 2. delphiha estimate")
    delphiha_round_3_lower = models.FloatField(doc="Lower bound of confidence interval on round 3. delphiha estimate")
    delphiha_round_3_upper = models.FloatField(doc="Lower upper of confidence interval on round 3. delphiha estimate")
    delphiha_round_4_lower = models.FloatField(doc="Lower bound of confidence interval on round 4. delphiha estimate")
    delphiha_round_4_upper = models.FloatField(doc="Lower upper of confidence interval on round 4. delphiha estimate")
    delphiha_round_5_lower = models.FloatField(doc="Lower bound of confidence interval on round 5. delphiha estimate")
    delphiha_round_5_upper = models.FloatField(doc="Lower upper of confidence interval on round 5. delphiha estimate")
    delphiha_round_6_lower = models.FloatField(doc="Lower bound of confidence interval on round 6. delphiha estimate")
    delphiha_round_6_upper = models.FloatField(doc="Lower upper of confidence interval on round 6. delphiha estimate")
    delphiha_round_7_lower = models.FloatField(doc="Lower bound of confidence interval on round 7. delphiha estimate")
    delphiha_round_7_upper = models.FloatField(doc="Lower upper of confidence interval on round 7. delphiha estimate")
    delphiha_round_8_lower = models.FloatField(doc="Lower bound of confidence interval on round 8. delphiha estimate")
    delphiha_round_8_upper = models.FloatField(doc="Lower upper of confidence interval on round 8. delphiha estimate")
    delphiha_round_9_lower = models.FloatField(doc="Lower bound of confidence interval on round 9. delphiha estimate")
    delphiha_round_9_upper = models.FloatField(doc="Lower upper of confidence interval on round 9. delphiha estimate")
    delphiha_round_10_lower = models.FloatField(doc="Lower bound of confidence interval on round 10. delphiha estimate")
    delphiha_round_10_upper = models.FloatField(doc="Lower upper of confidence interval on round 10. delphiha estimate")

    # Response Variables for Questionnaire
    gender = models.IntegerField(label="<b>Which gender do you identify with?</b>",
                               choices=[
                                   [1, 'female'],
                                   [2, 'male'],
                                   [3, 'other'],
                               ],
                                doc = "Questionnaire: Which gender do you identify with? "
                                      "(1: female, "
                                      "2: male"
                                      "3: other"
                                )
    education = models.IntegerField(label="<b>If you think back to your time since starting primary school, how many"
                                          " years have you been following a formal education (school, vocational"
                                          " training, university,etc.) until today?</b>",
                                    min=0,
                                    max=100,
                                    doc="If you think back to your time since starting primary school, how many"
                                          " years have you been following a formal education (school, vocational"
                                          " training, university,etc.) until today?")
    field_of_studies = models.IntegerField(label="<b> What describes your current/most recent field of study"
                                                 " best?</b>",
                                            choices=[
                                                [1, 'Business and/or Economics'],
                                                [2, 'Social Sciences'],
                                                [3, 'Natural Sciences'],
                                                [4, 'Arts'],
                                                [5, 'Other'],
                                                [6, 'I did/do not follow any studies']
                                                ],
                                           doc="Questionnaire: What describes your current/most recent field of study "
                                               "best?, (1: Business and/or Economics; 2: Social Sciences; 3: Natural"
                                               "Sciences; 4: Arts; 5: Other; 6: I did/do not follow any studies)")

    years_of_working = models.IntegerField(label="<b> Do you have professional working experience? If so, for how long?"
                                                 "</b>",
                                            choices=[
                                                [0, 'No, I do not have professional working experience'],
                                                [6, 'less than 1 year'],
                                                [1, '1 up to 2 years'],
                                                [2, '2 up to 3 years'],
                                                [3, '3 up to 4 years'],
                                                [4, '4 up to 5 years'],
                                                [5, '5 years or more'],
                                                ],
                                           doc="Questionnaire: Do you have professional working experience? If so, for"
                                               " how long? (0: No I do not have professional working experience;"
                                               "1: 1 year; 2: 2 years; 3: 3 years; 4: 4 years; 5: 5 years or more; "
                                               "6: less than 1 year)")
    # Honesty module
    honesty_A = models.IntegerField(doc="If I want something from a person I dislike, I will act very nicely toward"
                                         " that person in order to get it. (1: strongly disagree; 2;3;4; 5: strongly "
                                        "agree)"
                                   )
    honesty_B = models.IntegerField(doc="If I knew that I could never get caught, I would be willing to steal a million"
                                        " euro. (1: strongly disagree; 2;3;4; 5: strongly agree)"
                                   )
    honesty_C = models.IntegerField(doc="I wouldn't use flattery to get a raise or promotion at work, even if I thought"
                                        " it would succeed. (1: strongly disagree; 2;3;4; 5: strongly agree)"
                                   )
    honesty_D = models.IntegerField(doc="I would be tempted to buy stolen property if I were financially tight."
                                        "(1: strongly disagree; 2;3;4; 5: strongly agree)"
                                   )
    honesty_E = models.IntegerField(doc="If I want something from someone, I will laugh at that person's worst jokes."
                                        "(1: strongly disagree; 2;3;4; 5: strongly agree)"
                                   )
    honesty_F = models.IntegerField(doc="I would never accept a bribe, even if it were very large."
                                        "(1: strongly disagree; 2;3;4; 5: strongly agree)"
                                   )
    honesty_G = models.IntegerField(doc="I wouldn't pretend to like someone just to get that person to do favors for "
                                        "me. (1: strongly disagree; 2;3;4; 5: strongly agree)"
                                   )
    honesty_H = models.IntegerField(doc="I’d be tempted to use counterfeit money, if I were sure I could get away with"
                                        " it.(1: strongly disagree; 2;3;4; 5: strongly agree)"
                                    )

# PAGES
class Welcome(Page):
    form_model = 'player'
    form_fields = ['starting_time']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class TaskIntro(Page):
    form_model = 'player'
    form_fields = ['begintrial_time']

    @staticmethod
    def is_displayed(player: Player):
        if (
                player.round_number == 1
                and player.failed_attention_check == False
        ):
            return True

    @staticmethod
    def live_method(player: Player, data):
        if (
            data["information_type"] == "answer" and
            player.attention_check_tries == 1
        ):
            player.attention_check_1 = data["answer_q1"]
            player.attention_check_2 = data["answer_q2"]
            player.attention_check_3 = data["answer_q3"]
            player.attention_check_4 = data["answer_q4"]
            player.attention_check_5 = data["answer_q5"]
            player.attention_check_6 = data["answer_q6"]

        if (
                data["answer_q1"] == 2 and
                data["answer_q2"] == 3 and
                data["answer_q3"] == 1 and
                data["answer_q4"] == 1 and
                data["answer_q5"] == 3 and
                data["answer_q6"] == 2
        ):
            return{
                player.id_in_group: {"information_type": "no_error", "no_error": "Yeah!"},
            }
        else:
            player.failed_attention_check = True
            player.attention_check_tries = player.attention_check_tries + 1
            incorrect_answers = np.array([
                                data["answer_q1"] != 2,
                                data["answer_q2"] != 3,
                                data["answer_q3"] != 1,
                                data["answer_q4"] != 1,
                                data["answer_q5"] != 3,
                                data["answer_q6"] != 2,
                                ], dtype=bool)
            # incorrect_answers.np.astype(int)
            questions = ' and '.join(np.array(['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6'])[incorrect_answers])
            return{
                player.id_in_group: {"information_type": "error", "error": questions},
            }

class MyPage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        number_1 = random.randint(1,100)
        number_2 = random.randint(1,100)
        return{
            "number_1": number_1,
            "number_2": number_2,
        }

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [
    Welcome,
    TaskIntro,
    MyPage,
    ResultsWaitPage,
    Results
]
