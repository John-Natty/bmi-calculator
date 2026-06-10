# AI-IDE Workflow Integration - Mini Project

## Project Overview

This repository was created as part of the **AI-IDE Workflow Integration** project.

The goal of this project was to try different ways of using AI inside a code editor and to understand how an AI assistant can help a beginner read, write, improve, and debug code.

During this project, I tested:

* VS Code with an AI add-on
* Cursor, an AI-first code editor
* A browser AI helper such as ChatGPT
* AI completion
* AI chat
* AI agent mode

## Tools Used

For this project, I used the following AI-assisted tools:

* **VS Code** as a code editor
* **Codex** as an AI add-on inside VS Code
* **Cursor** as a second AI-first IDE
* **ChatGPT** as a browser AI helper for explanations and guidance

## AI Modes Practiced

### 1. Completion

Completion is when the AI suggests code directly inside the editor while typing.

I used completion to experience how an AI can quietly suggest the next part of the code.

### 2. Chat

Chat mode is when I ask the AI questions in a side panel.

I used chat to ask the AI to explain code, rewrite code in a beginner-friendly way, and help me understand the changes.

### 3. Agent Mode

Agent mode allows the AI to perform several steps on its own, such as creating folders, creating files, editing code, and reporting what it did.

I used agent mode to let the AI create a small project structure and generate files while I stayed in control of the changes.

## Mini Project: BMI Calculator

For the final tiny app, I created a beginner-friendly Python project that calculates a person's BMI.

BMI means Body Mass Index. It uses weight and height:

```text
BMI = weight / (height * height)
```

The program asks for:

* weight in kilograms
* height in meters

Then it prints:

* the BMI rounded to 2 decimals
* a simple health category

The program also handles invalid input, like text instead of numbers or values that are zero or negative.

## Files

```text
mini_project/
├── README.md
└── bmi_calculator.py
```

## How to Run

Run the program with:

```bash
python3 bmi_calculator.py
```

On some systems, you may need to use:

```bash
python bmi_calculator.py
```

## Example

```text
Enter your weight in kilograms: 70
Enter your height in meters: 1.75
Your BMI is: 22.86
Health category: Normal weight
```

## What I Learned

In this project, I learned that there are several ways to use AI inside a code editor.

VS Code with an AI add-on feels like a classic editor with AI added on top.

Cursor feels more directly focused on AI because the assistant is built into the editor from the start.

I also learned that AI can be helpful, but it should not be trusted blindly. It can suggest useful code, but I still need to read, test, and understand what it changes.

The developer must stay in control.
