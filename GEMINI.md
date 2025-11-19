# Project Overview

This directory contains the source files for the "Jupyter Guide to Linear Algebra," an interactive book created with Jupyter Book. The guide is designed for introductory-level students and covers core linear algebra topics using Python, NumPy, SciPy, and Matplotlib. It emphasizes practical computation and application over formal proofs and theorems.

The content is structured as a series of Jupyter notebooks (`.ipynb` files) that cover topics such as linear systems, vector spaces, linear transformations, inner products, and eigenvalues. The guide also includes introductions to Python, NumPy, and Jupyter itself.

A custom Python module, `laguide.py`, provides a set of functions for performing linear algebra operations like row reduction, QR factorization, and solving systems of equations. This module is used throughout the notebooks.

## Building and Running

This is a Jupyter Book project. To build the book locally, you need to have Python and the dependencies listed in `requirements.txt` installed.

1.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2.  **Build the book:**

    ```bash
    jupyter-book build .
    ```

This will generate a `_build/html` directory containing the static HTML files for the book. You can open `_build/html/index.html` in a web browser to view the book.

## Development Conventions

The project is organized as a Jupyter Book.

*   **Configuration:** The book's configuration is in `_config.yml`, which includes the title, author, and other settings.
*   **Table of Contents:** The structure of the book is defined in `_toc.yml`. This file determines the order of the chapters and sections.
*   **Content:** The main content is in the Jupyter notebooks (`.ipynb` files). Each notebook corresponds to a chapter or section of the book.
*   **Custom Module:** The `laguide.py` file contains custom functions used in the notebooks. Any new, reusable code should be added to this module.
*   **Images:** Images are stored in the `img/` directory.
*   **Solutions:** Solutions to exercises are provided in separate notebooks, such as `Linear_Systems_Solutions.ipynb`.
