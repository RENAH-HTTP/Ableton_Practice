# Report

## Monday, 11 May

#### Situation
- I noticed that values for parameters are put in brackets. 
- "Warning:" strucures are allowed.
- Also ":", also "()"

In this example - the "return track" is not capitalized: The original signal (which was received at Beat Repeat’s input) is mixed with Beat Repeat’s repetitions according to one of three mix modes: Mix allows the original signal to pass through the device and have repetitions added to it; Insert mutes the original signal when repetitions are playing but passes it otherwise; and Gate passes only the repetitions, never passing the original signal. Gate mode is especially useful when the effect is housed in a return track. Why?

Further more, release note structure is less rigid than the manual, leaving room for bullet point lists.

#### Task
Aimed to update the rules of writing the documentation of the desired Live element. And improve writing to match release note format. 

#### Action
Updated the linter app and added that to the extract rules at the bottom of this report.
Read the latest Release notes for Live 12.4 and 12.3 and extracted more style quides from there. 

#### Result
Improved quality and accuracy of replicating the format.
Defining clearly between Release note format and Manual format

## Sun, 10 May 

#### Situation
"behaviour" → "behavior" keeps appearing, passive voice is consistent and my biggest flag. Weak sentence openers are the second most often flag along with typos. 

#### Task
I aimed to learn what passive voice is and make a search for what weak sentence openers are. I felt I didn't understand exactly what those flags were so I set my self to deep search about those subjects. 

#### Action
Searched and learned what passive voice is, and what typical weak sentence openers are and how to avoid them...

#### Result
I learned the following: 
**Passive voice**
Passive voice: Passive voice is when the subject receives the action instead of doing it.
Latency is displayed (passive) - The display shows Latency (active) = always better to lead with the subject
**Weak openers**
Weak openers delay the real subject. The reader has to wade through "there is" or "it is" before getting to what actually matters.
**Introduction**
I can start with the active verb directly: "Choose", "Make", etc. 
or with a story way: Developed to achieve a natural sound, Formant Follow links formant movement to pitch movement for more natural results.

Rule: The fix for both is the same — find the real subject and lead with it. 

## Sat -> Sun, 9-10 May

#### Situation
Most of my texts weren't meeting the requirements.. or I thought the results were not trackable. I wanted to practice and needed the tool to understand the structure and the guides for writing documentation in the style of Ableton. 

#### Task
I owned it and analized that day from 15-17:00 the rules of writing documentation and the difference in format for the Manual, Release Notes and Bug Fixes. Task was to understand their underlying system to writing documentation and predict their guidelines. Added the notes from Ania and Lars after the interview. 

#### Action
Build a custom CLI application, since Git, runs from what I remembered mainly in CLI and I wanted to get even more confortable to terminal control. Exercised and got result that either my text was too long or too short (concisevness), i was unintentinally using passive voice, or that sometimes I still write in british english. I, also, update my mock-up website since I realized it needed a better structure to fit my current findings: bullet points were use only for bug fixes.

#### Result
Created a cleaner mock-up and had now the tools to keep improving. I now had some guidelines to work with: 
1. American English — No British spellings (colour → color, grey → gray, programme → program, etc.)
2. No marketing language — No exciting, powerful, innovative, seamless, revolutionary, game-changing, etc.
3. User-facing language — No developer jargon (implemented, refactored, backend, API call, hotfix, deprecated, etc.)
4. Do not start with I/We — Lead with the subject, the feature, or the action.
5. UI element capitalisation — Named UI elements are proper nouns (Arrangement View, Group Track, Auto Filter, Correction, Formant, etc.)
6. Acronym capitalisation — MIDI, MPE, CPU, GPU, VST, AU, AAX, DAW, LFO, ADSR, OSC are always all-caps.
7. No contractions — Use full forms: don't → do not, can't → cannot, it's → it is, etc.
8. Software name capitalisation — Live (the software) and version refs like Live 12 are always capitalised.
9. Grammar: allows/enables to — allows to and enables to are grammatically wrong. Use allows you to or lets you.
10. Paragraph length — Max 4 sentences per paragraph. (Not enforced in Free mode)
11. Passive voice — Avoid was added, has been updated, can be accessed. Use active voice.
12. Bug fix structure (Bug Fix mode) — Must describe both: what broke AND what now works.
13. Release note structure (Release Note mode) — Must lead with what the user can now DO.
14. Minimize words — Cut simply, just, easily, obviously, of course, clearly — they make tasks sound trivial.
15. Weak sentence opener — Avoid starting sentences with There is/are or It is. Lead with the real subject.
16. Redundant phrasing — in order to → to, due to the fact that → because, at this point in time → now, etc.
17. Filler phrases — Cut please note, note that, it is worth noting, as you can see, etc.
18. Double spaces — Single space between words and after punctuation.
19. Trailing ellipsis — ... at the end of a sentence implies an unfinished thought.
20. Avoid etc. — Complete the list or write and

#### Next-Steps
- ▢ Create a full release notes page for Live 12.4 with all new feature, improvements, and bug fix notes in the same structure as Ableton's official release notes page. This includes formatting according to all linter rules and no exceptions allowed.
- ▢ Include a before and after section on the documentation website. This includes one of the original stem separation release note changes from round one and one corrected with Ania's changes. Be sure to clearly label this section.
- ▢ Linter every piece of writing I produce and include an analysis in the daily STAR report of what was found, how it was fixed, and what was learned.
- ▢ Create a one page introduction to the writing style guide. Why we write for users, why we use active voice, why we use American English, why we be concise. How we got here and why.
- ▢ Create a full linter README file as proper documentation, including all installation steps, all rules and what they check for, examples and corrected code. This can be used as a documentation sample during the interview process.


# Rules for Writing
1. American English — No British spellings (colour → color, grey → gray, programme → program, etc.)
2. No marketing language — No exciting, powerful, innovative, seamless, revolutionary, game-changing, etc.
3. User-facing language — No developer jargon (implemented, refactored, backend, API call, hotfix, deprecated, etc.)
4. Do not start with I/We — Lead with the subject, the feature, or the action.
5. UI element capitalisation — Named UI elements are proper nouns (Arrangement View, Group Track, Auto Filter, Correction, Formant, etc.)
6. Acronym capitalisation — MIDI, MPE, CPU, GPU, VST, AU, AAX, DAW, LFO, ADSR, OSC are always all-caps.
7. No contractions — Use full forms: don't → do not, can't → cannot, it's → it is, etc.
8. Software name capitalisation — Live (the software) and version refs like Live 12 are always capitalised.
9. Grammar: allows/enables to — allows to and enables to are grammatically wrong. Use allows you to or lets you.
10. Paragraph length — Max 4 sentences per paragraph. (Not enforced in Free mode)
11. Passive voice — Avoid was added, has been updated, can be accessed. Use active voice.
12. Bug fix structure (Bug Fix mode) — Must describe both: what broke AND what now works.
13. Release note structure (Release Note mode) — Must lead with what the user can now DO.
14. Minimize words — Cut simply, just, easily, obviously, of course, clearly — they make tasks sound trivial.
15. Weak sentence opener — Avoid starting sentences with There is/are or It is. Lead with the real subject.
16. Redundant phrasing — in order to → to, due to the fact that → because, at this point in time → now, etc.
17. Filler phrases — Cut please note, note that, it is worth noting, as you can see, etc.
18. Double spaces — Single space between words and after punctuation.
19. Trailing ellipsis — ... at the end of a sentence implies an unfinished thought.
20. Avoid etc. — Complete the list or write and
21. Parameter Values - place parameter values in double quotes. 100% is "100%".

**Release Note Only**
1. Release note structure — must describe what the user can now DO (looks for: "can now", "lets you", "allows you", "use", "select", "access", etc.)

**Bug Fix Only**
1. Bug fix structure — must describe what broke (trigger condition) AND what now works (outcome after fix)

#### Update Log
- 11 May - added rule nr. 21 "Parameter Values"
- 09 May - Created the Rules list

# Questions

### 1. In this example - the **return track** is not capitalized:

```
The original signal (which was received at Beat Repeat’s input) is mixed with Beat Repeat’s repetitions according to one of three mix modes: Mix allows the original signal to pass through the device and have repetitions added to it; Insert mutes the original signal when repetitions are playing but passes it otherwise; and Gate passes only the repetitions, never passing the original signal. Gate mode is especially useful when the effect is housed in a return track.
```
- [Live Audio Effect Reference](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#live-audio-effect-reference)
- **Why, since it is a UI element?**
