# Kingdom Manager

A small Python project built to practice **Object-Oriented Programming (OOP)** — specifically **inheritance** — using a fantasy kingdom theme. It models different types of characters and structures in a kingdom, all built on top of a shared class hierarchy.

## Overview

This project demonstrates four core inheritance concepts in Python:

- **Single inheritance** — `Warrior` and `Mage` both inherit from `Character`
- **Multi-level inheritance** — `Paladin` inherits from `Warrior`, which inherits from `Character` (a three-level chain)
- **Multiple inheritance** — `GuardTower` inherits from both `Warrior` and `Building` at the same time
- **Method overriding** and **constructor chaining** using `super()` and direct parent calls

## Class hierarchy

```
Character
├── Warrior
│   ├── Paladin
│   └── (also used by) GuardTower
└── Mage

Building
└── (also used by) GuardTower

GuardTower(Warrior, Building)
```

## Classes

### `Character` (base class)
The foundation every character is built on.

| Attribute | Type | Description |
|---|---|---|
| `name` | str | The character's name |
| `health` | int | Starts at 100 |

| Method | Description |
|---|---|
| `introduce()` | Prints the character's name |
| `take_damage(amount)` | Reduces health by `amount` |
| `is_alive()` | Returns `True`/`False` based on health |
| `describe_role()` | Prints a generic role description (overridden by every subclass) |

### `Warrior(Character)`
Adds a `weapon` attribute and an `attack()` method.

### `Mage(Character)`
Adds a `mana` attribute and a `cast_spell()` method.

### `Paladin(Warrior)`
A specialized Warrior. Adds a `faith` attribute and a `smite()` method, which reuses `Warrior.attack()` via `super()` before adding its own effect.

### `Building`
A separate, unrelated class. Has a `durability` attribute and a `repair(amount)` method.

### `GuardTower(Warrior, Building)`
Inherits from **both** `Warrior` and `Building` — it can attack like a Warrior and be repaired like a Building. Its `__init__` calls each parent's constructor directly (`Warrior.__init__(self, ...)` and `Building.__init__(self, ...)`) to properly set up attributes from both sides.

## Project structure

```
kingdom-manager/
├── KingdomProject.py   # All class definitions
├── main.py             # Demo script that creates and tests every class
└── README.md           # This file
```

## Sample output

```
I am Ayesha.
Ayesha took 45 damage. Health is now 55.
True
I am just a generic character.
--------------------------------------------------------------------------------
Hadiqa attacks with a sword!
Warrior-Specific
I am Hadiqa.
True
--------------------------------------------------------------------------------
Zara casts a spell!
Mage-Specific
I am Zara.
True
--------------------------------------------------------------------------------
I am Sara.
Sara attacks with a hammer!
Sara attacks with a hammer!
Sara channels holy power!
Paladin-Specific
--------------------------------------------------------------------------------
110
--------------------------------------------------------------------------------
Ali attacks with a spear!
154
```

## Key concepts practiced

- Using `super().__init__(...)` to let a parent class handle its own setup instead of duplicating code
- Understanding **Method Resolution Order (MRO)** — the order Python looks through parent classes when using `super()`
- Handling **multiple inheritance** by calling each parent's `__init__` directly (`ParentClass.__init__(self, ...)`) when `super()` alone isn't enough
- Overriding methods (`describe_role()`) so each subclass behaves differently while sharing the same interface
- Keeping class-definition files free of test/demo code, and separating that into its own driver script (`main.py`)

## Author

Built by **Hadiqa Hanif** as a practice project for learning Python inheritance.
