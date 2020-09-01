# Karabiner Vim Mode Plus

A complex modification for [Karabiner Elements](https://karabiner-elements.pqrs.org/) that mimics [Vim's navigation](https://vim.fandom.com/wiki/Moving_around) throughout your entire Mac.

## So what do you get?

### NORMAL mode

* Activate with <kbd>caps lock</kbd>.
* Deactivate with:
  - <kbd>i</kbd> or <kbd>a</kbd> (there are more like these, see below)
  - <kbd>caps lock</kbd>,
  - <kbd>escape</kbd>,
  - <kbd>control</kbd>+<kbd>[</kbd>,
  - Clicking any mouse button
  - Pressing any key within Atom, iTerm2, PyCharm or VSCodium (because those have their own Vim modes)
  - Pressing any key while having at least one finger on your trackpad

Alternatively you can hold <kbd>caps lock</kbd> for NORMAL mode and release it to exit.

Within NORMAL mode you can then move around with:

key | action
--|--
<kbd>h</kbd> | Move cursor left*
<kbd>j</kbd> | Move cursor down*
<kbd>k</kbd> | Move cursor up*
<kbd>l</kbd> | Move cursor right*
<kbd>e</kbd> | Move cursor to next end of word
<kbd>b</kbd> | Move cursor to previous start of word
<kbd>0</kbd> | Move cursor to start of line
<kbd>^</kbd> | Move cursor to start of line
<kbd>$</kbd> | Move cursor to end of line
<kbd>g</kbd>,<kbd>g</kbd> | Move cursor to start of document
<kbd>G</kbd> | Move cursor to end of document
<kbd>{</kbd> | Move cursor to start of paragraph
<kbd>}</kbd> | Move cursor to end of paragraph

*These work with <kbd>shift</kbd>, <kbd>control</kbd>, <kbd>option</kbd> and/or <kbd>command</kbd>, e.g. for hotkeys within apps.

Combine those with <kbd>d</kbd>, <kbd>y</kbd> and <kbd>c</kbd> to delete (“cut”), yank (“copy”) or change (“cut” and exit NORMAL mode) like so:

key | action
--|--
<kbd>d</kbd>,<kbd>d</kbd>/<kbd>y</kbd>,<kbd>y</kbd>/<kbd>c</kbd>,<kbd>c</kbd> | Delete/yank/change the entire line
<kbd>d</kbd>,<kbd>e</kbd>/<kbd>y</kbd>,<kbd>e</kbd>/<kbd>c</kbd>,<kbd>e</kbd> | Delete/yank/change to the next end of word |
<kbd>d</kbd>,<kbd>b</kbd>/.../... | Delete/yank/change to the previous start of word
... | Likewise for all other navigation keys mentioned above

Also:

key | action
--|--
<kbd>x</kbd> | Delete forward
<kbd>X</kbd> | Delete back
<kbd>p</kbd> or <kbd>P</kbd> | Paste at cursor
<kbd>u</kbd> | Undo
<kbd>control</kbd>+<kbd>r</kbd> | Redo

To exit NORMAL mode at specific locations:

key | action
--|--
<kbd>i</kbd> | Exit NORMAL mode at the cursor
<kbd>I</kbd> | Exit NORMAL mode at the start of the line
<kbd>a</kbd> | Exit NORMAL mode at the cursor
<kbd>A</kbd> | Exit NORMAL mode at the end of the line
<kbd>o</kbd> | Exit NORMAL mode on a new line below the cursor
<kbd>O</kbd> | Exit NORMAL mode on a new line above the cursor

I've also mapped 3 keys to <kbd>F18</kbd>, <kbd>F19</kbd> and <kbd>F20</kbd>, which I pick up on within [Hammerspoon](https://www.hammerspoon.org/) to load specific modals:

key | action
--|--
<kbd>s</kbd> | Activate Hammerspoon screen modal
<kbd>m</kbd> | Activate Hammerspoon Markdown modal
<kbd>spacebar</kbd> | Activate Hammerspoon hyper modal

### VISUAL mode

From within NORMAL mode you can switch to VISUAL mode with <kbd>v</kbd>. (Unfortunately you cannot switch to the other end of the selection with <kbd>o</kbd> as you normally would, so choose your starting point wisely.)

key | action
--|--
<kbd>v</kbd> | Exit VISUAL mode, enter NORMAL mode
<kbd>h</kbd> | Select left
... | Likewise for all other navigation keys mentioned above
<kbd>d</kbd> | Delete (“cut”) the selection and enter NORMAL mode
<kbd>y</kbd> | Yank (“copy”) the selection and enter NORMAL mode
<kbd>c</kbd> | Change (“cut”) the selection and exit Vim Mode entirely
<kbd>x</kbd> | Remove the selection and enter NORMAL mode

## Setting up

1. Install Karabiner. (I use [the Homebrew cask](https://formulae.brew.sh/cask/karabiner-elements).)
2. Import this complex modification straight into Karabiner through the following link:

  [karabiner://karabiner/assets/complex_modifications/import?url=https://git.sr.ht/~harmtemolder/karabiner-vim-mode-plus/blob/master/vim_mode_plus.json](karabiner://karabiner/assets/complex_modifications/import?url=https://git.sr.ht/~harmtemolder/karabiner-vim-mode-plus/blob/master/vim_mode_plus.json)

## Making changes

I write my complex modifications in `YML` files, converting them into `JSON` using `yml-to-json.py`. You don't have to, but you can, if you want to. Either way, make sure to remove and re-add all parts of this mod in Karabiner's “Complex modifications” tab after making changes.

## Reporting issues

If you encounter any issues, please report them [here](https://todo.sr.ht/~harmtemolder/karabiner-vim-mode-plus). (For more info on sourcehut's issue tracker, see [this man page](https://man.sr.ht/todo.sr.ht/).)
