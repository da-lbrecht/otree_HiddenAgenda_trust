from otree.api import *
import random
import pandas

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'hiddenagenda_decisions'
    players_per_group = None
    num_trial_rounds = 4  # 1 round, i.e. judgment for trial evaluation from FTF, FTF+HA, Delphi and Delphi+HA each
    num_actual_rounds = 10  # 10 rounds, i.e. judgment for actual evaluation form FTF, FTF+HA, Delphi and Delphi+HA each
    num_rounds = 4 + 40

    fixed_pay = cu(10)
    avg_pay = cu(15)

    num_attention_checks = 5
    num_final_questions = 10
    num_interaction_formats = 4
    num_groups = 13  # number of groups per interaction format
    num_evaluations = 10  # number of evaluated judgments per interaction format by each group
    total_num_evaluations = 600

    # Group judgments
    trial_judgments = [20, 40, 60, 80]
    trial_judgment_origins = ["ftf", "ftf_ha", "delphi", "delphi_ha"]
    trial_true_values = [20, 40, 60, 80]

    actual_judgments_counter = list(range(1, num_trial_rounds + 1)) + \
                               list(range(1, num_evaluations + 1)) + list(range(1, num_evaluations + 1)) + \
                               list(range(1, num_evaluations + 1)) + list(range(1, num_evaluations + 1))

    interaction_formats = ["ftf", "ftf_ha", "delphi", "delphi_ha"]

    # Actual Judgments
    all_actual_judgments = list(pandas.read_csv("_static/data/judgments_artificial_trust_experiment(artificial600).csv")['group_estim'])

    # Underlying true values
    all_true_values = list(pandas.read_csv("_static/data/judgments_artificial_trust_experiment(artificial600).csv")['true_prob'])

    # Underlying origin
    all_origins = list(pandas.read_csv("_static/data/judgments_artificial_trust_experiment(artificial600).csv")['treatment'])

    # IDs of groups who conducted the judgment
    all_groups = list(pandas.read_csv("_static/data/judgments_artificial_trust_experiment(artificial600).csv")['group_id'])



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
    password = models.StringField(doc="Password needed to continue to actual rounds of task")

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
    trialRound = models.BooleanField(doc="1/True if round was a trial, without consequences for payment")
    judgmentOrigin = models.StringField(doc="Description of treatment of estimation study, from which group judgment"
                                            "originates")
    shuffle = models.IntegerField(doc="Randomization variable")
    judgment = models.FloatField(doc="Group judgment to be evaluated.")
    trueValue = models.FloatField(doc="true value underlying the group judgment.")
    judgmentLower = models.FloatField(doc="Lower bound of confidence interval on judgment from estimation study")
    judgmentUpper = models.FloatField(doc="Upper bound of confidence interval on judgment from estimation study")

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
    # Trust - GPS Question
    trust = models.IntegerField(doc="As long as I am not convinced otherwise, I assume that people have only the best"
                                "intentions."
                                    )

    # Task related questions
    understanding = models.IntegerField(doc="How would you rate your own understanding of the task you worked on "
                                            "throughout today's experiment?"
                                            "(1: very weak; 2;3;4; 5: very good)"
                                        )
    strategy = models.StringField(label="How did you come up with a range around the group judgments, based on the"
                                        " information your were given?",
                                  doc="How did you come up with a range around the group judgments, based on the"
                                      " information your were given?",
                                  blank=True
                                  )
    hidden_agendas = models.StringField(label="Did you evaluate group judgments from groups with hidden agendas "
                                              "differently? How?",
                                        doc="Did you evaluate group judgments from groups with hidden agendas "
                                            "differently? How?",
                                        blank=True
                                        )
    wish = models.StringField(label="If you wanted to get the judgment of a group of people, of which some have"
                                    " a hidden agenda, how would you like that group to interact?",
                              doc="If you wanted to get the judgment of a group of people, of which some have"
                                    " a hidden agenda, how would you like that group to interact?",
                              blank=True
                              )


# FUNCTIONS

# Randomization of task round display
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        list_of_round_ids = list(range(1, Constants.num_trial_rounds + 4 * Constants.num_evaluations + 1))

        # Create list of ids of all judgments
        ftf_shuffle = list(range(0, 150))
        ftfha_shuffle = list(range(150, 300))
        delphi_shuffle = list(range(300, 450))
        delphiha_shuffle = list(range(450, 600))
        # Randomize judgments within block
        random.shuffle(ftf_shuffle)
        random.shuffle(ftfha_shuffle)
        random.shuffle(delphi_shuffle)
        random.shuffle(delphiha_shuffle)
        shuffle = ftf_shuffle + ftfha_shuffle + delphi_shuffle + delphiha_shuffle
        for player in subsession.get_players():
            for i in list_of_round_ids:
                if i <= Constants.num_trial_rounds:
                    player.in_round(i).shuffle = 999
                elif Constants.num_trial_rounds < i <= Constants.num_trial_rounds + 1 * Constants.num_evaluations:
                    player.in_round(i).shuffle = int(shuffle[
                                                         int(i - 5 + round(round((player.id_in_group-2)/3, 0) * 7.8, 0))
                                                             ]
                                                     )
                elif i <= Constants.num_trial_rounds + 2 * Constants.num_evaluations:
                    player.in_round(i).shuffle = int(shuffle[
                                                         int(i + 150 - 15 + round(round((player.id_in_group-2)/3, 0) * 7.8, 0))
                                                             ]
                                                     )
                elif i <= Constants.num_trial_rounds + 3 * Constants.num_evaluations:
                    player.in_round(i).shuffle = int(shuffle[
                                                         int(i + 300 - 25 + round(round((player.id_in_group-2)/3, 0) * 7.8, 0))
                                                             ]
                                                     )
                elif i <= Constants.num_trial_rounds + 4 * Constants.num_evaluations:
                    player.in_round(i).shuffle = int(shuffle[
                                                         int(i + 450 - 35 + round(round((player.id_in_group-2)/3, 0) * 7.8, 0))
                                                             ]
                                                     )
                if i <= Constants.num_trial_rounds:
                    player.in_round(i).judgment = Constants.trial_judgments[i-1]
                    player.in_round(i).trueValue = Constants.trial_judgments[i-1]
                    player.in_round(i).judgmentOrigin = Constants.trial_judgment_origins[i-1]
                if i > Constants.num_trial_rounds:
                    player.in_round(i).judgment = round(Constants.all_actual_judgments[player.in_round(i).shuffle]*100, 1)
                    player.in_round(i).trueValue = round(Constants.all_true_values[player.in_round(i).shuffle]*100, 1)
                    player.in_round(i).judgmentOrigin = Constants.all_origins[player.in_round(i).shuffle]
                    player.in_round(i).shuffled_judgmentGroup = Constants.all_groups[player.in_round(i).shuffle]

# PAGES
class Welcome(Page):
    form_model = 'player'
    form_fields = ['starting_time']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class TaskIntro(Page):
    form_model = 'player'
    form_fields = [
        'begintrial_time',
    ]

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


class TrialCompleted(Page):
    form_model = 'player'
    form_fields = ['password']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == (Constants.num_trial_rounds + 1)

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['password'] != '1984':
            return 'Password incorrect'


class NewInteraction(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        if (
                player.round_number == Constants.num_trial_rounds + 1 * Constants.num_evaluations + 1 or
                player.round_number == Constants.num_trial_rounds + 2 * Constants.num_evaluations + 1 or
                player.round_number == Constants.num_trial_rounds + 3 * Constants.num_evaluations + 1
        ):
            return True
        else:
            return False

    @staticmethod
    def vars_for_template(player: Player):
        previous_interaction_format = \
            player.in_round(player.round_number - 1).judgmentOrigin
        if previous_interaction_format == 'ftf':
            return {
                "previous_interaction_format": 'face-to-face groups'
            }
        elif previous_interaction_format == 'ftf_ha':
            return {
                "previous_interaction_format": 'face-to-face groups with hidden agendas'
            }
        elif previous_interaction_format == 'delphi':
            return {
                "previous_interaction_format": 'delphi groups'
            }
        elif previous_interaction_format == 'delphi_ha':
            return {
                "previous_interaction_format": 'delphi groups with hidden agendas'
            }


class Task(Page):
    form_model = 'player'
    form_fields = [
        'end_of_round',
        'judgmentLower',
        'judgmentUpper'
    ]

    @staticmethod
    def is_displayed(player: Player):
        if (
                player.round_number <= Constants.num_rounds
        ):
            return True

    @staticmethod
    def vars_for_template(player: Player):
        group_judgment = f'"{player.judgment}"'
        true_value = player.trueValue
        judgment_origin = player.judgmentOrigin
        first_rounds = [
            Constants.num_trial_rounds + 1,
            Constants.num_trial_rounds + 1*Constants.num_evaluations + 1,
            Constants.num_trial_rounds + 2*Constants.num_evaluations + 1,
            Constants.num_trial_rounds + 3*Constants.num_evaluations + 1
                        ]
        judgment_counter = Constants.actual_judgments_counter[player.round_number - 1]
        return {"round_number": player.round_number,
                "group_judgment": group_judgment,
                "true_value": true_value,
                "judgment_origin": judgment_origin,
                "num_trial_rounds": Constants.num_trial_rounds,
                "judgment_counter": judgment_counter,
                "num_evaluations": Constants.num_evaluations,
                "first_rounds": first_rounds,
                "shuffled_round": player.shuffle,
                }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.round_number <= Constants.num_trial_rounds:
            player.trialRound = True
        else:
            player.trialRound = False
        if player.round_number == Constants.num_trial_rounds:
            player.end_of_trial = player.end_of_round


class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['gender', 'education', 'field_of_studies', 'years_of_working',
                   'trust', 'understanding', 'strategy', 'hidden_agendas', 'wish']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds


class Results(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player: Player):
        random_draw = random.choice(list(range(Constants.num_trial_rounds + 1,
                                               Constants.num_trial_rounds + 4 * Constants.num_evaluations + 1)))
        if player.in_round(random_draw).judgmentOrigin == 'ftf':
            drawn_judgment_origin = 'face-to-face groups'
        elif player.in_round(random_draw).judgmentOrigin == 'ftf_ha':
            drawn_judgment_origin = 'face-to-face groups with hidden agendas'
        elif player.in_round(random_draw).judgmentOrigin == 'delphi':
            drawn_judgment_origin = 'delphi groups'
        elif player.in_round(random_draw).judgmentOrigin == 'delphi_ha':
            drawn_judgment_origin = 'delphi groups with hidden agendas'
        drawn_judgment = f'"{player.in_round(random_draw).judgment}"'
        drawn_judgment_counter = Constants.actual_judgments_counter[player.in_round(random_draw).round_number - 1]
        drawn_true_value = player.in_round(random_draw).trueValue
        drawn_lower_limit = player.in_round(random_draw).judgmentLower
        drawn_upper_limit = player.in_round(random_draw).judgmentUpper
        if drawn_lower_limit <= drawn_true_value <= drawn_upper_limit:
            hit = 1
        else:
            hit = 0
        interval = drawn_upper_limit - drawn_lower_limit
        if hit:
            bonus = round(2 * (10 * (1 - (drawn_upper_limit - drawn_lower_limit) / 100))) / 2
        else:
            bonus = 0
        player.payoff = bonus
        total_payoff = bonus + player.session.config['participation_fee']
        return {
            "random_draw": random_draw,
            "drawn_judgment_origin": drawn_judgment_origin,
            "drawn_judgment": drawn_judgment,
            "drawn_true_value": drawn_true_value,
            "drawn_lower_limit": drawn_lower_limit,
            "drawn_upper_limit": drawn_upper_limit,
            "interval": interval,
            "hit": hit,
            "bonus": cu(bonus),
            "total_payoff": total_payoff,
            "num_evaluations": Constants.num_evaluations,
            "drawn_judgment_counter": drawn_judgment_counter,
        }


page_sequence = [
    # Welcome,
    # TaskIntro,
    TrialCompleted,
    NewInteraction,
    Task,
    # Questionnaire,
    Results
]
