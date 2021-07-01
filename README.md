# Data Engineering @ PeakData

The goal of this task is to recreate a minimal working scenario of data engineers at PeakData, in order to see the following:

- Ability to manipulate data using modern Python data tools
- Knowledge of Python best practices
- Ability to decompose tasks and high-level thinking
- Basic programming principles

## Task

Given a list of medical publications, provide a list of unique authors and institutions.

Note that authors can appear in multiple publications and may have slight differences in their names, initials, etc. between articles.

In addition to your code, we expect a `README.md` containing:
- How to build and run the code
- Documentation on your approach, i.e. what did you do and why?
- A reporting of potential failure points and bottlenecks
- An accounting of the remaining steps needed before putting deploying your code to a production system

### Input

The full input csv can be found in this repository. Here we provide an example:

`publications_min.csv.gz`:

| temp_id | abstract | title | pubdate | journal | affiliations | publication_uuid | authors |
| ------- | -------- | ----- | ------- | ------- | ------------ | ---------------- | ------- |
| 0 | "The pulmonary effects of hyperventilation following infusion of sodium salicylate into the cisterna magna was studied in 16 spontaneously breathing adult sheep. We found a fall in PaO2, a decrease in the static compliance of the respiratory system, abnormal chest roentgenographic films, and grossly abnormal lungs following 3.5 to 13 h of hyperventilation..." | Acute respiratory failure following pharmacologically induced hyperventilation: an experimental animal study. | 1988-01-01 00:00:00 | "Intensive care medicine, Issue: 1, Volume: 15 1988" | "National Institutes of Health, Laboratory of Technical Development, Bethesda, Maryland., , , , , " | 0.0 | "['D Mascheroni', 'T Kolobow', 'R Fumagalli', 'M P Moretti', 'V Chen', 'D Buckhold']" |
| 1 | "Ten patients with acute respiratory failure (ARF), (4 pneumonia, 4 sepsis, 2 polytrauma), underwent computerized tomography (CT) of the lungs, (apex, hilum, base), at 5, 10, 15 cm H2O positive end expiratory pressure (PEEP)..." | Morphological response to positive end expiratory pressure in acute respiratory failure. Computerized tomography study. | 1986-01-01 00:00:00 | "Intensive care medicine, Issue: 3, Volume: 12 1986" | ", , , , , , , , , " | 1.0 | "['L Gattinoni', 'D Mascheroni', 'A Torresin', 'R Marcolin', 'R Fumagalli', 'S Vesconi', 'G P Rossi', 'F Rossi', 'S Baglioni', 'F Bassi']" |

### Expected output

`unique_people.csv`:

| firstname | lastname |
| --------- | -------- |
| Reinhard | Dummer |
| Alexander | Navarini |
| Gerhard | Rogler |
| Pierre | Michetti |
| Gerhard | Garhöfer |
| Stephan | Hoffmann |

## Time is limited

We understand your time is precious and would not want you to spend more than `2 to 4 hours over the span of one week`. The outcome should be locally runnable on a UNIX-flavored OS (MacOS, Linux).

It is OK if the challenge is not completed. Try to prioritize by what you think is most important. Tell us what motivated your choices, how you tackled the task, what you would do differently were you given more time, what you would differently a second time around, etc.

## Submission

Please zip and email your solution to `ethan@peakdata.com`. We will confirm your submission and get back to you about next steps within 1 week.
