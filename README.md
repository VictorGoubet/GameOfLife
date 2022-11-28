[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
<a name="readme-top"></a>



<br />
<div align="center">
  <a href="https://github.com/VictorGoubet/GameOfLife">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRq4fznCFt-0SH25M9VBnb9DF_RXRG4y9aX0_J5tcX4d4xFsGQvmEEBrVw1zEPNw5AxyVg&usqp=CAU" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Conway's Game of Life</h3>

  <p align="center">
    <i>What if the life was governed by three laws ?</i>
    <br />
    <a href="https://github.com/VictorGoubet/GameOfLife/blob/master/GameOfLife.py"><strong>Check the code »</strong></a>
    <br />
    <br />
    <a href="https://github.com/VictorGoubet/GameOfLife/issues">Report Bug</a>
    •
    <a href="https://github.com/VictorGoubet/GameOfLife/issues">Request Feature</a>
  </p>
</div>





## About The Project
</br>

[![Product Name Screen Shot][product-screenshot]](screenshot.PNG)

The game of life is a automaton where each cell is represented as a simple square. If the square is black, the cell is alive, if not, the cell is dead. The goal is to simulate the evolutions there life cycle using the following simple rules:

* Any live cell with fewer than two live neighbours dies (referred to as underpopulation).
* Any live cell with more than three live neighbours dies (referred to as overpopulation).
* Any live cell with two or three live neighbours lives, unchanged, to the next generation.
* Any dead cell with exactly three live neighbours comes to life.


<p align="right"><a href="#readme-top">🔝</a></p>


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

You will just need python >= 3.0. You can check the version by using the following command.

  ```sh
  > python -V
  > 3.0.0
  ```

### Installation

You can follow the different steps inorder to get the programm working on your computer


1. Clone the repo
   ```sh
   git clone https://github.com/VictorGoubet/GameOfLife.git
   ```
2. Install python packages
   ```sh
   pip install -r requirements.txt
   ```
3. Be free to modify the parameters in the **GameOfLife.py** class
   ```py
   game = GameOfLife(epochs=50, n_cells=20, windows_size=600)
   ```
4. Execute the python script
   ```sh
   python GameOfLife.py
   ```

The windows should appear! The interface is pretty intuitive, have fun!

<p align="right"><a href="#readme-top">🔝</a></p>





<!-- CONTACT -->
-----
</br>

[![LinkedIn][linkedin-shield]][linkedin-url]
</br>
Victor Goubet - victorgoubet@orange.fr  


<!-- MARKDOWN LINKS & IMAGES -->
[forks-shield]: https://img.shields.io/github/forks/VictorGoubet/GameOfLife.svg?style=for-the-badge
[forks-url]: https://github.com/VictorGoubet/GameOfLife/network/members
[stars-shield]: https://img.shields.io/github/stars/VictorGoubet/GameOfLife.svg?style=for-the-badge
[stars-url]: https://img.shields.io/github/issues/VictorGoubet/GameOfLife/stargazers
[issues-shield]: https://img.shields.io/github/issues/VictorGoubet/GameOfLife.svg?style=for-the-badge
[issues-url]: https://github.com/VictorGoubet/GameOfLife/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/victorgoubet/
[product-screenshot]: screenshot.PNG
