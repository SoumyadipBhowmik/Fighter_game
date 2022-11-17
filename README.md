# DUEL IT OUT

A short game project on duel made from scratch using the pygame module.

> Here are some screenshots from the game

<table>
<td><img src= "Readme Stuff\Game Overlook1.png" height = "320"></td>
<td><img src= "Readme Stuff\Game Overlook3.png" height = "320"></td>
</table>

> Here's a video on the game

<video align = "center" height = "320" controls autoplay><source src = "Readme Stuff\gameVideo.mp4"></video>

# GAME FEATURES

> I could've implemented more features into this game but I'm only a beginner and learning

<ul>
<li>5 in-game characters</li>
<li>2 players can play on the same screen</li>
<li>Individual sounds for individual characters</li>
<li>Background Sound and Countdown during start</li>
<li>Added an immovable but parallex background for an eye pleasing effect</li>
<li>Has a main menu but it's not that great. Neither does it have multiple features</li>
</ul>

# GETTING STARTED WITH THE GAME

> I could've made this into an .EXE file but lot of things won't work.

<ol>
<li>Fork this repository</li>
<li>Open up your IDE. I prefer VS Code since it's lightweight but powerful</li>
<li>Make Sure you have python 3.10+ installed</li>
<li>Clone the forked repository</li>
<li>Run it. Play it. Enjoy it.</li>
<li>If you like this game, Star this repository so I can get more motivation to create what I've started</li>
</ol>

# PLAYING THE GAME
<details><summary>👈Click for Player 1 controls</summary>
A and D: Moves left and right

W: Jump

J: Attack 1

K: Attack 2
</details>
<details><summary>👈Click for Player 2 controls</summary>

Left Arrow and Right Arrow Key: Moves left and right

UP Arrow Key: Jump

NUMPAD 1: Attack 1

NUMPAD 2: Attack 2
</details>

# CHARACTERS
#### Here's how you can use different characters in game

```
Step 1: In main.py, find line numbers: 36, 37, 106, 107
Step 2: Replace the sentence after "=" by character lists given in the drop-down below
This works for both player 1 and player 2
```
<details><summary>👈Character list</summary>

#### FIGHTER
```
Fighter(1, 225, 425, False, FIGHTER_DATA, fighter_sheet, FIGHTER_ANIMATION_LIST, human_sword, sword_fx2, human_sword, sword_fx2, jump1)
```
#### MASKED SAMURAI
```
Fighter(2, 720, 420, True, MASKED_SAMURAI_DATA, masked_samurai_sheet, MASKED_SAMURAI_ANIMATION_LIST, unsheathSound, sword_fx2, unsheathSound, sword_fx2, jump2)
```
#### TRIBAL WARRIOR
```
Fighter(1, 220, 420, False, JUNGLE_WARRIOR_DATA, jungle_warrior_sheet, JUNGLE_WARRIOR_ANIMATION_LIST, human_sword, sword_fx2, human_sword, sword_fx2, jump1)
```
#### ASSASSIN WARRIOR
```
Fighter(2, 720, 420, True, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_LIST, sword_fx1, sword_fx2, lightning_fx, lightning_fx2, jump2)
```
#### WIZARD

> I didn't add any sound effects for wizard since I am not a fan of magic and fantasy but its easy to add
```
Fighter(2, 720, 420, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_LIST, sword_fx1, sword_fx2, lightning_fx, lightning_fx2, jump2)
```
</details>

# CREDIT WHERE ITS DUE
Game is inspired from <a href = "https://www.youtube.com/channel/UCPrRY0S-VzekrJK7I7F4-Mg">Code With Russ</a>---> @russs123

Incredible sprites created by <a href = "https://luizmelo.itch.io/">Luiz Melo </a>

Background has been taken from <a href = "https://twitter.com/twistedsifter">TwistedSifter</a>

# CONTRIBUTING
Any meaningful contributions are warmly welcomed.