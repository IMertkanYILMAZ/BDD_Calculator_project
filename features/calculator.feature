Feature: Calculator

  Scenario Outline: Ask for calculator type
    Given I open the calculator
    When the calculator shows the menu and the user inputs <type1>
    Then then the user selected the type

  Examples: Calc Type
    | type1   |
    | Sum     |
    | scientific    |
    | yanlis  |

  Scenario Outline: User inputs wrong calculator type
    Given I open the calculator
    When the calculator shows the menu and the user inputs <type1>
    Then the warning message is returned to the user

  Examples: Calc Type Wrong
    | type1   |
    | yanlis dene     |
    | yanlis  |

  Scenario Outline: Add two numbers
    Given I entered <numb1>
    And and <numb2> to the calculator
    When I press add
    Then The result is <result1>

  Examples: Summation
    | numb1   | numb2   | result1 |
    | 5       | 12      | 17      |
    | 10      | 1       | 11.0    |
    | 5       | -9      | -4      |
    | denebeni     | 9       |Wrong Input|

  Scenario Outline: Subtract two numbers
    Given I entered <numb1>
    And and <numb2> to the calculator
    When I press subtract
    Then The result is <result1>

  Examples: Summation
    | numb1   | numb2   | result1 |
    | 5       | 12      | -7      |
    | 10      | 1       | 9       |
    | 5       | -9      | 14      |

  Scenario Outline: Multiply two numbers
    Given I entered <numb1>
    And and <numb2> to the calculator
    When I press multiplication
    Then The result is <result1>

  Examples: Multiplication
    | numb1   | numb2   | result1 |
    | 5       | 12      | 60      |
    | 10      | -1      | -10     |
    | 5       | 0       | 0       |

  Scenario Outline: Divide two numbers
    Given I entered <numb1>
    And and <numb2> to the calculator
    When I press division
    Then The result is <result1>

  Examples: Division
    | numb1   | numb2   | result1              |
    | 5       | 1       | 5                    |
    | 10      | -1      | -10                  |

  Scenario Outline: Divide by zero
    Given I entered <numb1>
    And and <numb2> to the calculator
    When I press division
    Then The user gets Zero Division Error

  Examples: Division by zero
    | numb1   | numb2   |
    | 5       | 0       |
    | 10      | 0       |

  Scenario Outline: Scientific calculator
    Given I entered calculator type <calc_type>
    And I entered <equ1>
    When I press calculate
    Then The result is <result1>

  Examples: Summation
    |calc_type  | equ1    | result1     |
    |scientific | 5+3-2   | 6           |
    |scientific | 10/2+4  | 9           |
    |scientific | 2*3/0   | Wrong Input |

