# Mitigating Manipulation in Committees: Experiment Codebase

This repository contains the oTree implementation of the **decision experiment** used in my research project:

**Albrecht, David. _Mitigating manipulation in committees: Just let them talk!_**  
Working paper (SSRN): https://ssrn.com/abstract=5994274

## Research context

Many high-stakes decisions are made by small groups (committees, boards, and teams). This project studies how group interaction format and strategic manipulation incentives affect:

- objective judgment accuracy,
- information sharing,
- and perceived trustworthiness.

The broader paper compares two interaction formats:

1. **Face-to-face (FTF)** interaction in video calls.
2. **Delphi-style** structured, pseudonymous interaction.

Both are tested with and without **hidden agendas** (private side-payment incentives for manipulation).

## What this repository implements

This repository implements the **second experimental part** (decision experiment):

- Individual participants evaluate previously generated group judgments
- **4 trial rounds** (one per treatment condition)
- **40 payoff-relevant rounds** (10 judgments per condition)
- Incentivized confidence-interval elicitation around group judgments
- A **2x2 treatment design** inherited from the estimation experiment (interaction format × hidden agenda incentives)

### Treatment conditions represented in data

- `ftf`: Face-to-face, no hidden agenda incentives
- `ftf_ha`: Face-to-face, with hidden agenda incentives
- `delphi`: Delphi-style structured interaction, no hidden agenda incentives
- `delphi_ha`: Delphi-style structured interaction, with hidden agenda incentives

## Experimental flow (implemented)

Participants complete:

1. Welcome, data policy, and informed consent
2. Instruction phase with video and comprehension checks
3. Trial block with 4 practice evaluations (not payoff-relevant)
4. 40 randomized evaluation rounds across all treatment conditions
5. Post-experiment questionnaire (demographics, work experience, trust item, strategy reflections)
6. Payoff screen with one randomly drawn paying round

### Key design mechanics reflected in code

- **Balanced randomization**: treatment block order is randomized per participant while preserving balance across the lab session.
- **Within-block randomization**: judgments are shuffled within each treatment block.
- **Live comprehension checks**: instruction checks are validated in real time, including retry feedback.
- **Incentive-compatible scoring**: participants report lower/upper bounds around judgments; narrower correct intervals earn higher bonuses.
- **Linked two-stage design**: all evaluated judgments come from the first-stage group estimation experiment.

## Data used by this app

The app reads evaluation targets from `_static/data/judgments_trust_experiment_(600).csv`:

- **600 observations** total
- **150 observations per condition** (`ftf`, `ftf_ha`, `delphi`, `delphi_ha`)
- Core fields used in runtime logic:
  - `group_estim` (group judgment)
  - `true_prob` (underlying true value)
  - `treatment`
  - `group_id`

## Technical implementation highlights

- Built with **oTree 5.4.1**.
- Implements multi-page workflow logic in `HiddenAgenda_trust/__init__.py`.
- Uses **live page methods** for attention-check validation and participant feedback.
- Captures rich process data (timing, round-level interval choices, questionnaire responses, payoff components).
- Uses custom HTML/CSS/JavaScript UI for interval elicitation and treatment-specific instruction framing.

## Local setup

### 1) Clone

```bash
git clone git@github.com:da-lbrecht/otree_HiddenAgenda_trust.git
cd otree_HiddenAgenda_trust
```

### 2) Python environment and dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3) Run locally

```bash
otree devserver
```

Then open: http://localhost:8000/

## Configuration notes

- Session configuration is defined in `settings.py` (`HiddenAgenda_trust` app sequence).
- `OTREE_ADMIN_PASSWORD` should be set via environment variable for admin access.
- The file `Creating a session` documents lab operations for balanced assignment (single session, 50 participants, chronological link usage).

## Citation

If you use this codebase for academic work, please cite:

Albrecht, David. _Mitigating manipulation in committees: Just let them talk!_ Working paper. SSRN: https://ssrn.com/abstract=5994274

## License

This project is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. See `LICENSE`.
