# oTree Trust Experiment: Hidden Agendas in Group Judgments

This repository contains the full oTree implementation of one experiment from the research project:

**Albrecht, David — _Mitigating Manipulation in Committees: Just let them talk!_**  
Working Paper (SSRN): https://ssrn.com/abstract=5994274

Specifically, this code implements the **decision experiment** that measures the **perceived trustworthiness** of group judgments generated in a prior estimation experiment.

## Why this project matters

Many high-stakes decisions are made by small groups (committees, boards, teams). Some members may have hidden agendas and strategically manipulate outcomes. This project operationalizes a behavioral experiment that quantifies:

- how interaction format affects group-judgment accuracy under manipulation,
- how participants perceive trustworthiness of those judgments,
- and where objective accuracy and perceived trust diverge.

In this second-stage decision experiment, participants evaluate judgments produced under four treatment conditions:

- face-to-face (`ftf`)
- face-to-face with hidden agendas (`ftf_ha`)
- Delphi (`delphi`)
- Delphi with hidden agendas (`delphi_ha`)

## What this code does

The app runs a complete participant workflow for eliciting confidence intervals around historical group judgments.

### Participant flow

1. **Welcome, data policy, consent** (`Welcome`)
2. **Instruction phase with video and live attention checks** (`TaskIntro`)
3. **Short transition page before incentivized rounds** (`TrialCompleted`)
4. **4 trial rounds** (one per interaction format; unpaid)
5. **40 incentivized rounds** (`Task`)  
	 - 10 judgments per treatment condition
	 - treatment blocks randomized across participants
	 - judgment order randomized within blocks
6. **Transition pages between treatment blocks** (`NewInteraction`)
7. **Closing survey** (`Questionnaire`)
8. **Payoff feedback with randomly selected paying round** (`Results`)

### Incentive mechanism

Participants submit a lower and upper bound around each displayed group judgment (0–100 scale). One incentivized round is randomly selected for payment.

- If the true value lies **inside** the interval, bonus increases as interval width decreases.
- If the true value lies **outside** the interval, bonus is 0.
- Total payment = fixed participation fee + bonus.

## Data pipeline used in the app

The app loads a precompiled dataset of group judgments:

- file: `_static/data/judgments_trust_experiment_(600).csv`
- observations: **600**
- treatment balance: **150 observations** per treatment (`ftf`, `ftf_ha`, `delphi`, `delphi_ha`)
- key fields used by the app:
	- `group_estim` (group judgment)
	- `true_prob` (underlying true value)
	- `treatment`
	- `group_id`

## Technical implementation highlights

This project showcases applied research engineering in an experimental-economics setting:

- **oTree-based experiment orchestration** with multi-page workflow and round logic
- **Within-subject treatment randomization** with balanced block-order assignment
- **Incentive-compatible payoff computation** in server-side logic
- **Live validation of comprehension checks** via `live_method`
- **Comprehensive response logging** (timing, choices, survey responses)
- **Custom participant UI** (Bootstrap + custom JS slider interaction)

## Repository structure

- `HiddenAgenda_trust/__init__.py` — core app logic (models, randomization, payoff, page sequence)
- `HiddenAgenda_trust/*.html` — participant-facing pages (instructions, task, survey, results)
- `_static/data/judgments_trust_experiment_(600).csv` — judgments evaluated in this experiment
- `settings.py` — oTree session/app configuration
- `Creating a session` — operational note for lab deployment

## Local setup

### 1) Clone

```bash
git clone git@github.com:da-lbrecht/otree_HiddenAgenda_trust.git
cd otree_HiddenAgenda_trust
```

### 2) Create environment and install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3) Run locally

```bash
otree devserver
```

Then open `http://localhost:8000/`.

## Running sessions (lab operations)

Operational note from `Creating a session`:

- create one session with 50 participants,
- keep the server running across lab waves,
- assign participant links chronologically to preserve balanced randomization.

## Research context

This code corresponds to the decision study that elicits perceived trustworthiness of judgments generated in the estimation study. The design compares judgments from face-to-face and Delphi groups, each with and without hidden agendas, allowing analysis of how manipulation and communication format affect trust and accuracy.

## Citation

If you use this repository or build on this experiment design, please cite:

> Albrecht, David. _Mitigating Manipulation in Committees: Just let them talk!_ Working Paper. SSRN: https://ssrn.com/abstract=5994274

## License

This project is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

See [LICENSE](LICENSE) and [LICENSE.md](LICENSE.md).
