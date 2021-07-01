# Data Engineering @ PeakData

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

# Solution

Because amount of given data is quite small, I've decided to build small POC instead of running server which is capable of processing stream of data. I can fit whole dataset in a single DataFrame and process it on local notebook. 

I was mainly focused on finding simplest solution and then iterate with small improvments.
From my perspective it is better, to deliver partial working solution, than stay in progresss forever.

### Local enviroment
Use python 3.9
T
```
# Preparation of local enviroment
python -m venv venv
source venv/bin/activate
pip install -r requirements-freeze.txt
jupyter notebook
```

To run my code, just open `solution.ipynb` in the browser and run all cells.

## Names

At first, I had to unwrap authors column, at first I supposed it is a valid json, but after receiving a lot of errors I've deiced that manual extraction is necessary. 

I assumed that first_name and last_name are first and last word from the string.

I wanted to translate single letter abbrevionts, with matching based on surnames. (For matched surname, find name starting on specific letter). But in that case, I'm not extending unique list of people, because I'm extending it with already existing people.
After this consideration I've decided to drop inputs with single letters as names. 
For final tuning I'm only accepting names without special charters.

### Potential failure points
* In some cases last_name is composed of more than one word. We do not take this possibility into account.
* We ommit a person, when it has only a record with first_name as abbreviation. If such person is not presented in the data with full first_name, we droped it

## Affiliations

Extracting names of institiutons is even more complicated. I've tried to split them by commas, but very often commas are a part of a long name with city, country and so on.

After exploring the data, I found out that very often with the institute we are also provided with the country name. My approach was to split strings on country names. This would a separator for diffrent affiliations. 

It works most of the time, but sometimes catches country name from university name, not from "address". I run out of time, but more sophisticated solution for this splitting should be possible.

### Potential failure points
* splitting is not perfect. One record may contain parts of diffrent Universities names
* Our comparison is very naive (to_lower + duplicates). (Bag of words / n-grams) approach could give more in depth similarity relation.

## Possible Production
To move this solution to production we have to add tests, logging, and metrics.
I would deploy it on AWS because I have most experience with that cloud provider.