from otree.api import *
import random

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'hiddenagenda_decisions'
    players_per_group = None
    num_trial_rounds = 4  # 1 round, i.e. judgment for trial evaluation from FTF, FTF+HA, Delphi and Delphi+HA each
    num_actual_rounds = 40  # 10 rounds, i.e. judgment for actual evaluation form FTF, FTF+HA, Delphi and Delphi+HA each
    num_rounds = 4 + 40

    fixed_pay = cu(10)
    avg_pay = cu(15)

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

    # Group judgments for trial round
    group_judgments = [20, 40, 60, 80]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Process variables
    starting_time = models.LongStringField(doc="Time at which Informed Consent is given and experiment starts")
    begintrial_time = models.LongStringField(doc="Time at which the whole trial started")

    end_of_trial = models.StringField(initial=999,
                                      doc="Time at which the whole trial period was completed")
    start_of_round = models.StringField(initial=999,
                                        doc="Starting time of a task round")
    end_of_round = models.StringField(initial=999,
                                      doc="Ending time of a task round")

    round_displayed = models.IntegerField(doc="Randomized round displayed to participants, ranging from 1 to "
                                              "num_rounds")

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
    estimate_1_lower = models.FloatField(doc="Lower bound of confidence interval on 1. task round in estimation study")
    estimate_1_upper = models.FloatField(doc="Lower upper of confidence interval on 1. task round in estimation study")
    estimate_2_lower = models.FloatField(doc="Lower bound of confidence interval on 2. task round in estimation study")
    estimate_2_upper = models.FloatField(doc="Lower upper of confidence interval on 2. task round in estimation study")
    estimate_3_lower = models.FloatField(doc="Lower bound of confidence interval on 3. task round in estimation study")
    estimate_3_upper = models.FloatField(doc="Lower upper of confidence interval on 3. task round in estimation study")
    estimate_4_lower = models.FloatField(doc="Lower bound of confidence interval on 4. task round in estimation study")
    estimate_4_upper = models.FloatField(doc="Lower upper of confidence interval on 4. task round in estimation study")
    estimate_5_lower = models.FloatField(doc="Lower bound of confidence interval on 5. task round in estimation study")
    estimate_5_upper = models.FloatField(doc="Lower upper of confidence interval on 5. task round in estimation study")
    estimate_6_lower = models.FloatField(doc="Lower bound of confidence interval on 6. task round in estimation study")
    estimate_6_upper = models.FloatField(doc="Lower upper of confidence interval on 6. task round in estimation study")
    estimate_7_lower = models.FloatField(doc="Lower bound of confidence interval on 7. task round in estimation study")
    estimate_7_upper = models.FloatField(doc="Lower upper of confidence interval on 7. task round in estimation study")
    estimate_8_lower = models.FloatField(doc="Lower bound of confidence interval on 8. task round in estimation study")
    estimate_8_upper = models.FloatField(doc="Lower upper of confidence interval on 8. task round in estimation study")
    estimate_9_lower = models.FloatField(doc="Lower bound of confidence interval on 9. task round in estimation study")
    estimate_9_upper = models.FloatField(doc="Lower upper of confidence interval on 9. task round in estimation study")
    estimate_10_lower = models.FloatField(
        doc="Lower bound of confidence interval on 10. task round in estimation study")
    estimate_10_upper = models.FloatField(
        doc="Lower upper of confidence interval on 10. task round in estimation study")

    # Response Variables for Questionnaire
    gender = models.IntegerField(label="<b>Which gender do you identify with?</b>",
                                 choices=[
                                     [1, 'female'],
                                     [2, 'male'],
                                     [3, 'other'],
                                 ],
                                 doc="Questionnaire: Which gender do you identify with? "
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


# FUNCTIONS

# Randomization of task round display
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        list_of_trial_round_ids = list(range(1, Constants.num_trial_rounds + 1))
        list_of_actual_round_ids = list(range(Constants.num_trial_rounds + 1, Constants.num_actual_rounds + 2))
        list_of_round_ids = list(range(1, Constants.num_trial_rounds + 1))
        subsession_trial_temp_list = list_of_trial_round_ids
        subsession_actual_temp_list = list_of_actual_round_ids
        # Randomizing
        random.shuffle(subsession_trial_temp_list)
        random.shuffle(subsession_actual_temp_list)
        for player in subsession.get_players():
            temp_list = subsession_trial_temp_list + subsession_actual_temp_list
            for i in list_of_round_ids:
                player.in_round(i).round_displayed = temp_list[i - 1]


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
            return {
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
            return {
                player.id_in_group: {"information_type": "error", "error": questions},
            }


class Task_Trial(Page):
    form_model = 'player'
    form_fields = [
        'end_of_round'
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number <= 4

    @staticmethod
    def vars_for_template(player: Player):
        group_judgment = f'"{Constants.group_judgments[player.round_displayed-1]}"'
        group_judgment_ll = f'"{ max(Constants.group_judgments[player.round_displayed-1]-1,0) }"'
        group_judgment_ul = f'"{ min(Constants.group_judgments[player.round_displayed-1]+1,100) }"'
        if player.round_number <= 4:
            return {"round_number": player.round_number,
                    "round_displayed": player.round_displayed,
                    "group_judgment": group_judgment,
                    "group_judgment_ll": group_judgment_ll,
                    "group_judgment_ul": group_judgment_ul,
                    }
        else:
            pass

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.round_number == 4:
            player.end_of_trial = player.end_of_round
        else:
            pass


class Results(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 8


page_sequence = [
    # Welcome,
    # TaskIntro,
    Task_Trial,
    Results
]
