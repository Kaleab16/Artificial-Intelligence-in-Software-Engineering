# AI: Dynamic Web Lab Generation for Core CSS Concepts

## Objective

This project demonstrates the use of sequential AI prompting to generate interactive web-based learning tools for core CSS concepts.

The labs use HTML, CSS, and JavaScript in single-file web applications to make CSS behavior visible and interactive.

## Files

### 1. `initial-box-model.html`

The initial Box Model Lab generated from the first AI prompt.

It demonstrates:

- CSS Box Model
- Content, padding, border, and margin
- Box width
- `display` property
- `block`
- `inline-block`
- `inline`
- Real-time CSS updates using JavaScript

### 2. `refined-box-model.html`

The refined version generated after applying a second AI prompt.

It adds:

- Individual margin controls for top, right, bottom, and left
- Individual padding controls for top, right, bottom, and left
- Individual border-width controls
- Corner-radius control

### 3. `flexbox-grid-playground.html`

An interactive playground for exploring CSS Flexbox and Grid.

It allows users to experiment with:

- `display`
- Flex direction
- Flex wrapping
- Justify content
- Align items
- Grid columns
- Grid rows
- Grid auto-flow
- Gap
- Dynamic items

## AI Workflow

The project was created using a sequential prompting workflow.

### Prompt 1 — Initial Box Model Lab

The first prompt established the basic requirements for the Box Model learning environment.

### Prompt 2 — Refinement

The second prompt extended the first application by adding individual controls for each side of the margin, padding, and border, along with border-radius.

### Prompt 3 — Flexbox/Grid Playground

A separate AI conversation was used to generate an interactive playground for CSS Flexbox and Grid.

## Learning Reflection

Interactive web labs make CSS concepts easier to understand because changes can be observed immediately instead of only reading about them in documentation or looking at static diagrams. For example, changing the `display` property from `block` to `inline` makes the difference in layout behavior visible immediately. The controls also make it easier to understand how padding, margin, border, and width affect the size and position of an element.

The sequential prompting approach was useful because each prompt had a focused purpose. The first prompt established a working Box Model lab, while the second prompt refined that existing application instead of requiring everything to be specified at once. This is similar to real software development, where a basic implementation is created first and then improved through additional requirements and iterations. The third prompt applied the same idea to a separate Flexbox and Grid playground.
