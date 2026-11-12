# Python Selenium Automation Suite 🐍🤖

A comprehensive test automation framework and practice repository built using **Python** and **Selenium WebDriver**, structured to demonstrate proficiency in handling diverse web elements, browser actions, data-driven testing, and testing frameworks.

---

## 🚀 Key Features & Covered Modules

This repository is organized into structured modules covering standard and complex test automation scenarios:

*   **Locators & Elements:** Absolute/Relative XPaths[cite: 3], CSS Selectors[cite: 3], and inspection of disabled elements[cite: 3].
*   **Browser Interactions & Handling:**
    *   **Dropdowns & Frames:** Single/multiple dropdowns[cite: 1], nested and multi-frames[cite: 1].
    *   **Popups & Alerts:** JavaScript alerts, authentication popups, and hidden division alerts[cite: 2].
    *   **Windows & Tabs:** Multi-window switching and handling browser tabs[cite: 2].
    *   **Mouse & Keyboard Operations:** Click & Hold, Drag & Drop, Mouse Hover, Actions class, and horizontal/vertical JavaScript scrolling[cite: 2].
    *   **Dynamic Web Tables:** Handling dynamic rows/columns and data extraction[cite: 2].
*   **Data-Driven Testing (DDT):** Reading and writing test data using Excel (`openpyxl`) integrated with modular utility scripts[cite: 1].
*   **Advanced Configurations:**
    *   Headless browser testing and persistence configuration ("To stay on browser")[cite: 2, 3].
    *   Automated screenshot capture (including exception-triggered screenshots)[cite: 3].
*   **Frameworks & Test Practice:**
    *   **PyTest Integration:** Modular test files with `conftest.py` setup[cite: 3].
    *   **Real-World Scenarios:** Automated test scripts for search workflows, university portals, and e-commerce platforms (e.g., Amazon, ShopperStack)[cite: 3].

---

## 🛠️ Tech Stack

*   **Language:** Python[cite: 1, 2, 3]
*   **Automation Tool:** Selenium WebDriver[cite: 1, 2, 3]
*   **Test Framework:** PyTest[cite: 3]
*   **Data Handling:** Openpyxl (Excel Utilities)[cite: 1]
*   **IDE:** PyCharm

---

## 📂 Project Structure

```text
PythonProject/
│
├── Selenium Testing/
│   ├── Broken Elements/      # Broken links & image validation
│   ├── DDT/                  # Data-Driven Testing & Excel utilities
│   ├── Handling/             # Checkboxes, radio buttons, date pickers, dropdowns, frames
│   ├── Keyboard Operation/   # Keyboard actions automation
│   ├── Links/                # Link validation scripts
│   ├── Mouse Operations/     # Hover, drag-and-drop, scroll actions
│   ├── Popups and Alerts/    # Handling JS, auth, and hidden alerts
│   ├── Web Tables/           # Dynamic table data parsing
│   ├── Window or Tab/        # Window/Tab switching utilities
│   ├── Headless Testing/     # Headless mode configurations
│   ├── Locators/             # XPath & CSS locator strategies
│   ├── Practice/             # End-to-end site test scripts (Amazon, ShopperStack)
│   ├── PyTest/               # PyTest fixtures and structured test scripts
│   └── ScreenShots/          # Captured failure/success screens
