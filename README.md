# Report

## Friday, 15 May

#### Situation
Three real entries from Ableton release notes. Unclear which tense rule applies to which.

1. "The filter decay in Drum Sampler's 8bit effect can now be disabled by turning the decay parameter all the way up."
2. "Parameter naming for the delay sections across devices has been improved."
3. "Added new Audio Effect Racks (Vocal Strip Complete, Guitar Amp Stack)."

#### Task
Build a tense map — when do we use which form.

#### Action

Entry 1 → Release note. Present tense. "can now" = new user capability. ✓

Entry 2 → Past passive. Vague. "has been improved" doesn't say what changed for the user.
Better: "Delay section parameter names are now consistent across devices."

Entry 3 → Past participle. "Added" = changelog bullet style.
Weaker than user-facing. "You can now use Vocal Strip Complete and Guitar Amp Stack Audio Effect Racks." is stronger.

Bug/fix entries → passive voice is standard here. "Fixed an issue where X was Y."
Not the same as doc passive — it's the required form for fixes. Prominently passive, intentionally.

Release notes = user perspective first. "Added X" = product side. "You can now use X" = user side. Always the second.

#### Result

Tense map:

- Bug / Fix → past tense, passive is standard. "Fixed an issue where..."
- Release note → present tense, user-first. "X can now Y." / "On [Platform], it is now possible to..."
- Changelog bullet → past participle. "Added X." / "Improved Y." / "Updated Z."
- Manual / instruction → imperative or present. "Select X", "Click Y", "Use X to Y"

Key rule: release notes frame from the user's perspective, not the product's.

---

## Thursday, 14 May 

#### Situation
Release notes have different rules depending on what type of change it is. Updates, fixes, bugs — past tense, passive voice. Platform-specific stuff — you lead with the platform name. "On Windows,...", "On macOS,...". 

Also ran into this example: "On Windows, it is now possible to navigate Live's browser forward and back with the mouse browser navigation buttons. This feature works when Live's browser is in focus." — wait, isn't browser a UI element? Should that be Browser? 

#### Task
Get the tense/voice rules straight for each release note type. Figure out if browser counts as a UI element or not.

#### Action
Tested a few release note entries against the patterns. Updates and bugs consistently use past passive — "was added", "was fixed", "has been updated". Platform entries always open with "On [Platform]:" and use present tense after. Two different contexts, two different rules.

For browser — open question. It behaves like a named component. Probably should be capitalized. Ask the team.

Updated the linter to reflect what I learned — added checks for past tense passive in fix/update entries and the "On [Platform]:" prefix pattern. Also created a dedicated Bug Fix Rules section at the bottom of this report next to the main rules.

#### Result
Two rules:

1. Updates / fixes / bugs — past tense, passive voice.
   "The issue was fixed where...", "A new option was added..."

2. Platform-specific updates — lead with "On [Platform]:"
   Present tense follows. "On macOS, it is now possible to..."

3. Browser — probably a UI element. Probably Browser. Not confirmed yet.

## Wednesday, 13 May

#### Situation
Writing release notes and documentation, unsure when "is now" / "are now" constitutes passive voice. Also questioning whether documentation needs to be perfect before shipping. Additionally unclear on the correct naming conventions for UI elements.

My linter also doesn't flag future passive voice constructions in the type "You will be remembered by"

#### Task

Clarify the passive voice rule around linking verbs. Internalize a working principle for documentation quality vs. user priority. Research correct terminology for common UI element types. Add future check to linter app. 

#### Action 

Tested "is now" and "are now" against the passive voice rule — passive requires to be + past participle. Linking verbs don't qualify. Confirmed "is now Pack Overview" is clean.

Researched UI element naming conventions — toggle, chooser, button, slider, field, dialog box, prompt — and established a working rule: name elements by their behavior, not their appearance. When in doubt, open Live and observe what the element does.

Drew on a real conversation with my supervisor at MSM about standardizing metadata guidelines — learned that perfect standardization is rarely achievable in practice.

Add passive voice future check for linter app.. but also ask if it is a rule.

#### Result

Three rules internalized:

1. "is now" and "are now" are linking verbs — safe to 
   use, not passive voice.

2. Don't chase perfection. Prioritize the user. 
   If it makes sense to the person reading it, 
   it's good enough to ship.

3. Name UI elements by behavior not appearance — 
   open Live and observe when uncertain.

4. Ask Sara or Lars if the passive voice is a rule.
    Or is it for present and not for future? 

## Tuesday, 12 May

#### Situation
THe Delay LFO device: two parameters — Wave and Morph — that users would need more documentation. (Wander) has ambiguous generation behavior. Morph's effect varies per shape — mechanism unknown.

#### Task
1. Document all 7 wave shapes with one-line active-voice descriptions.
2. Clarify Wander — is it a continuously generated random signal, or does it trigger per cycle?
3. Clarify Morph — what exactly does it transform per shape?
4. Write the Morph parameter description once both unknowns resolved.

#### Action
Sine + Morph: "Morph skews the sine peak toward the rising or falling edge."
Square + Morph: "Morph adjusts the pulse width of the square wave."
These are hypothetical until confirmed. I have to ask the documentation team... 

#### Result
Passive-voice patterns identified and corrected. Morph partial draft ready. Two blockers surfaced as explicit questions rather than undocumented assumptions.


## Monday, 11 May

#### Situation
- I noticed that values for parameters are put in brackets. 
- "Warning:" strucures are allowed.
- Also ":", also "()"

In this example - the "return track" is not capitalized: The original signal (which was received at Beat Repeat’s input) is mixed with Beat Repeat’s repetitions according to one of three mix modes: Mix allows the original signal to pass through the device and have repetitions added to it; Insert mutes the original signal when repetitions are playing but passes it otherwise; and Gate passes only the repetitions, never passing the original signal. Gate mode is especially useful when the effect is housed in a return track. Why?

- Further more, release note structure is less rigid than the manual, leaving room for bullet point lists.
- Problems with passive voice. Example: "In the dedicated Link page new features were added:". Passive voice. 

#### Task
Aimed to update the rules of writing the documentation of the desired Live element. And improve writing to match release note format. 

Fix passive voice.

#### Action
Updated the linter app and added that to the extract rules at the bottom of this report.
Read the latest Release notes for Live 12.4 and 12.3 and extracted more style quides from there. 

- Taking more notes on passive voice

#### Result
Improved quality and accuracy of replicating the format.

Defining clearly between Release note format and Manual format

- New info: "In the dedicated Link page new features were added:". Passive voice. The subject ("new features") is receiving the action rather than performing it.

Found a gimmik to see if a text is passive voice or not 

The zombie test: 

"Two noise types are included in Erosion by zombies" — grammatically fine, so it's passive.

"Erosion includes two noise types by zombies" — doesn't work, so it's active. 

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

# Bug Fix Rules

1. Always lead with "Fixed" — "Fixed an issue where...", "Fixed a bug where...", "Fixed a crash that occurred when..."
2. Platform-specific bugs — name the platform first. "Fixed an issue on macOS where...", "Fixed an issue on Windows where..."
3. Describe the trigger — what action or condition caused the bug. Be specific.
4. Describe the outcome — what now works. Can be a second sentence: "X now Y."
5. Passive voice IS allowed here — "Fixed an issue where X was not Y" is the standard form. The linter skips passive checks in Bug Fix mode.
6. Use bullet points for multiple related fixes in the same release.
7. No crash without a trigger — "Fixed a crash" alone is not enough. State what caused it.
8. All standard rules still apply — American English, UI element caps, no marketing, no dev jargon, no contractions, acronym caps, etc.

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

### 2. Does Wander continuously generate a new random signal (smooth, unsynced, always moving), or does it produce a new random shape once per LFO cycle? 

```
Select one of the following LFO waveforms via the Wave drop-down: Sine, Triangle, Ramp Up, Ramp Down, Square, S&H (Sample and Hold), or Wander. You can further shape the selected waveform using the Morph slider.
```
- [Live Audio Effect Reference](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#live-audio-effect-reference)

- **Does Wander continuously generate a new random signal?**

### 3. What does Morph specifically transform for each wave shape? For example — does it change pulse width on Square, skew the peak on Sine, bend the slope on Triangle? 

```
Select one of the following LFO waveforms via the Wave drop-down: Sine, Triangle, Ramp Up, Ramp Down, Square, S&H (Sample and Hold), or Wander. You can further shape the selected waveform using the Morph slider.
```

- [Live Audio Effect Reference](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#live-audio-effect-reference)

- **Does Wander continuously generate a new random signal?**

3. Is future passive voice permitted? 

```
You will then be prompted to select a tag group or parent tag for the newly created tag. Type the name of an existing tag group or parent tag, or type your desired name and select either the Create new parent tag… or Create new tag group… option.
``` 

Also here: 

```
Note that this mode is not yet implemented in Live, but is expected to be implemented in a future update.
```

- [Release Notes Live 12.4](https://www.ableton.com/en/release-notes/live-12/)

4. How can we decide what tense we use?

```
The filter decay in Drum Sampler's 8bit effect can now be disabled by turning the decay parameter all the way up.
```

```
Parameter naming for the delay sections across devices has been improved.
```

this could be just improved something

```
Added new Audio Effect Racks (Vocal Strip Complete, Guitar Amp Stack). - for example ere we use added?
```

for example we use added?

5. Duplicate!

```
Fixed an issue where it was not possible to navigate back to the Splice label with the Browse Back and Browse Forward buttons after navigating to other labels in the browser. This change also makes it possible to use these buttons to navigate to the Cloud label even when Cloud is not authorized, as well as to the Max for Live label even when Max is not available.
```
