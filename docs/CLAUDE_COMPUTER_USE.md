# Claude Computer Use for Desktop Testing

## Purpose

This document explains how Claude Computer Use can support desktop application testing.

The main use case considered here is testing QGIS plugins and other graphical desktop applications.

---

## What Is Claude Computer Use?

Claude Computer Use allows an AI agent to interact with graphical user interfaces.

Instead of working only with source code or command-line tools, the agent can:

- observe screenshots,
- identify visible interface elements,
- move the pointer,
- click buttons and menus,
- type text,
- use keyboard shortcuts,
- observe the result of an action.

This makes it suitable for testing applications that require direct interaction with a desktop interface.

---

## Why Desktop Testing Is Different

Browser testing usually provides structured information such as:

- HTML,
- DOM elements,
- selectors,
- URLs,
- browser automation APIs.

Desktop applications may not expose the same structure.

A desktop test may therefore depend on:

- application windows,
- menus,
- dialogs,
- screen coordinates,
- keyboard input,
- mouse interaction,
- operating-system permissions,
- window focus.

This makes desktop testing generally more environment-dependent than browser testing.

---

## QGIS Example

For the QGIS plugin template, a Computer Use test could perform the following workflow:

1. Start QGIS.
2. Open the Plugins menu.
3. Select Institution Plugin Template.
4. Click Open Widget Examples.
5. Verify that the plugin dialog opens.
6. Verify that the expected widget examples are visible.
7. Enter text into QLineEdit.
8. Select an item from QComboBox.
9. Toggle QCheckBox.
10. Change QSpinBox or QSlider values.
11. Verify that the interface remains responsive.
12. Record the test result.

---

## Relation to the Current Desktop Test

The current desktop test uses macOS System Events and AppleScript.

It verifies:

- that QGIS becomes the active application,
- that the expected plugin dialog window is open.

Example expected window:

`Institution Plugin Template - Widget Examples`

This provides deterministic operating-system-level verification.

Claude Computer Use could extend this by performing visual interaction with the widgets inside the dialog.

---

## Possible Test Result

The test should return one of:

- PASS
- FAIL
- BLOCKED

### PASS

The required interface was opened and the expected interactions were completed successfully.

### FAIL

The application was available, but the expected behavior was incorrect.

### BLOCKED

The test could not be completed because of an environment, permission, dependency, or automation limitation.

---

## Advantages

Computer Use can help test:

- applications without browser DOM access,
- native desktop interfaces,
- complex multi-step user workflows,
- visual interaction paths,
- menu and dialog behavior.

It can also simulate behavior closer to a real user.

---

## Limitations

Desktop testing with computer-use agents may be affected by:

- screen resolution,
- window position,
- application startup time,
- unexpected dialogs,
- operating-system permissions,
- UI layout changes,
- visual ambiguity,
- focus problems.

Because of these limitations, Computer Use should not be treated as the only verification method.

Whenever possible, it should be combined with deterministic checks such as:

- unit tests,
- integration tests,
- application logs,
- accessibility APIs,
- operating-system-level checks.

---

## Recommended Strategy

For QGIS plugin testing, a layered approach can be used:

1. Python syntax and unit checks.
2. QGIS plugin load verification.
3. Operating-system-level desktop verification.
4. Computer Use for visual interaction.
5. Review of the collected evidence.

This provides stronger verification than relying on a single testing method.