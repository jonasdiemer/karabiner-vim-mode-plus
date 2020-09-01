# Karabiner Vim Mode Plus

A complex modification for [Karabiner Elements](https://karabiner-elements.pqrs.org/) that mimics [Vim's navigation](https://vim.fandom.com/wiki/Moving_around) throughout your entire Mac.

## 1. So what do you get?

### 1.1 NORMAL mode

* Activate with <code>caps lock</code>.
* Deactivate with:
  - <code>i</code> or <code>a</code> (there are more like these, see below)
  - <code>caps lock</code>,
  - <code>escape</code>,
  - <code>control</code>+<code>[</code>,
  - Clicking any mouse button
  - Pressing any key within Atom, iTerm2, PyCharm or VSCodium (because those have their own Vim modes)
  - Pressing any key while having at least one finger on your trackpad

Alternatively you can hold <code>caps lock</code> for NORMAL mode and release it to exit.

Within NORMAL mode you can then move around with:

key | action
--- | ---
<code>h</code> | Move cursor left*
<code>j</code> | Move cursor down*
<code>k</code> | Move cursor up*
<code>l</code> | Move cursor right*
<code>e</code> | Move cursor to next end of word
<code>b</code> | Move cursor to previous start of word
<code>0</code> | Move cursor to start of line (before any tabs)
<code>^</code> | Move cursor to start of line (after any tabs)
<code>$</code> | Move cursor to end of line
<code>g</code>,<code>g</code> | Move cursor to start of document
<code>G</code> | Move cursor to end of document
<code>{</code> | Move cursor to start of paragraph
<code>}</code> | Move cursor to end of paragraph

*These work with <code>shift</code>, <code>control</code>, <code>option</code> and/or <code>command</code>, e.g. for hotkeys within apps.

Combine those with <code>d</code>, <code>y</code> and <code>c</code> to delete (“cut”), yank (“copy”) or change (“cut” and exit NORMAL mode) like so:

key | action
--- | ---
<code>d</code>,<code>d</code> / <code>y</code>,<code>y</code> / <code>c</code>,<code>c</code> | Delete/yank/change the entire line
<code>d</code>,<code>e</code> / <code>y</code>,<code>e</code> / <code>c</code>,<code>e</code> | Delete/yank/change to the next end of word |
<code>d</code>,<code>b</code> / ... / ... | Delete/yank/change to the previous start of word
... | Ditto for all other navigation keys mentioned above

Also:

key | action
--- | ---
<code>x</code> | Delete forward
<code>X</code> | Delete back
<code>p</code> or <code>P</code> | Paste at cursor
<code>u</code> | Undo
<code>control</code>+<code>r</code> | Redo

To exit NORMAL mode at specific locations:

key | action
--- | ---
<code>i</code> | Exit NORMAL mode at the cursor
<code>I</code> | Exit NORMAL mode at the start of the line
<code>a</code> | Exit NORMAL mode at the cursor
<code>A</code> | Exit NORMAL mode at the end of the line
<code>o</code> | Exit NORMAL mode on a new line below the cursor
<code>O</code> | Exit NORMAL mode on a new line above the cursor

I've also mapped 3 keys to <code>F18</code>, <code>F19</code> and <code>F20</code>, which I pick up on within [Hammerspoon](https://www.hammerspoon.org/) to load specific modals:

key | action
--- | ---
<code>s</code> | Activate Hammerspoon screen modal
<code>m</code> | Activate Hammerspoon Markdown modal
<code>spacebar</code> | Activate Hammerspoon hyper modal

### 1.2 VISUAL mode

From within NORMAL mode you can switch to VISUAL mode with <code>v</code>. (Unfortunately you cannot switch to the other end of the selection with <code>o</code> as you normally would, so choose your starting point wisely.)

key | action
--- | ---
<code>v</code> | Exit VISUAL mode, enter NORMAL mode
<code>h</code> | Select left
<code>j</code> | Select down
... | Ditto for all other navigation keys mentioned above
<code>d</code> | Delete (“cut”) the selection and enter NORMAL mode
<code>y</code> | Yank (“copy”) the selection and enter NORMAL mode
<code>c</code> | Change (“cut”) the selection and exit Vim Mode entirely
<code>x</code> | Remove the selection and enter NORMAL mode

## 2. Setting up

1. Install Karabiner. (I used [this Homebrew cask](https://formulae.brew.sh/cask/karabiner-elements) through `brew cask install karabiner-elements`.)
2. Import this complex modification straight into Karabiner through this link:

    <a href="karabiner://karabiner/assets/complex_modifications/import?url=https://git.sr.ht/~harmtemolder/karabiner-vim-mode-plus/blob/master/vim_mode_plus.json" target="_blank">karabiner://karabiner/assets/complex_modifications/import?url=https://git.sr.ht/~harmtemolder/karabiner-vim-mode-plus/blob/master/vim_mode_plus.json</a>

    (You might have to copy and paste it into your browser's address bar if your browser does not render it as a clickable link.)

## 3. Making changes

I write my complex modifications in `YML` files, converting them into `JSON` using `yml-to-json.py`. You don't have to, but you can, if you want to. Either way, make sure to remove and re-add all parts of this mod in Karabiner's “Complex modifications” tab after making changes. The order they are in is important.

## 4. Reporting issues

If you encounter any issues, please report them [here](https://todo.sr.ht/~harmtemolder/karabiner-vim-mode-plus). (If you need help with sourcehut's issue tracker, see [this man page](https://man.sr.ht/todo.sr.ht/).) I'd also love to hear additions you would like to see to this setup.
