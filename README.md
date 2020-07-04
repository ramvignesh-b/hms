
<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="static/img/logo.svg" alt="Logo" width="180" height="180">
  </a>

  <h2 align="center">Hospital Management System</h2>
  <h5 align="center"><em>(Using Flask)</em></h5>

  <p align="center">
    <br />
    <a href="https://github.com/ayushgd/hms/docs/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="http://hms-tcs.el.r.appspot.com" target="_blank">View Demo</a>
    ·
    <a href="https://github.com/ayushgd/hms/issues">Report Bug | Request features</a>
    ·
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://hms-tcs.el.r.appspot.com)

This project was done as a part of TCS Xplore Case Study, by a team of 4 soon-to-be TCSers, with a sprint goal set to deliver a MVP of HMS. This application meets the end user specification but has it's features limited to the functional requirements mentioned in the SRS, due to a short time frame of 6 days. That being said, it's a possibility to add new features to this app over time. Fell free to create a PR and implement any features that you'd like to be a part of this application.

### Built With

* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [Flask](https://palletsprojects.com/p/flask/)



<!-- GETTING STARTED -->
## Getting Started

Clone the repository to get started

### Prerequisites

* [python](https://www.python.org/)

### Installation

1. Clone the repo
```sh
git clone https://github.com/ayushgd/hms.git
```
2a. Create a Virtual Environment (Optional)
```sh
python -m venv .hms
```
2b. Activate the virtual environment 
```sh
.hms\Scripts\activate
```
3. Install the requirements and dependancies
```sh
pip install -r requirements.txt
```
4. Run the application
```python
flask run
```
5. View the application on localhost
```
http://localhost:5000/
```


### Usage

#### Login Credentials:

* Admin Executive
```sh
Username: 12345678@A
Password: 12345678@A
```

* Pharmacist
```sh
Username: 12345678@P
Password: 12345678@P
```

* Diagnostic Executive
```sh
Username: 12345678@D
Password: 12345678@D
```

*Note While creating new login credentials please set the ending character with accordance to the role of the stakeholder.*

    * Admission Desk Executive/Registration Desk executive: A
    * Pharmacist: P
    * Diagnostic Executive: D


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

* RamVignesh B. - [![linkedin-shield]](https://linkedin.com/in/ramvigneshb) - ramvignesh.codes@gmail.com
* Ayush Saini - [![linkedin-shield]](https://www.linkedin.com/in/ayush-saini-570345137/) - ayushgd@gmail.com
* Vibhor Aggarwal - [![linkedin-shield]](https://www.linkedin.com/in/vibhor-aggarwal-6585a5185/) - vibhor.msn@gmail.com
* Chittaranjan Sahu - [![linkedin-shield]](https://www.linkedin.com/in/chittaranjan-sahu-7a7289129/) - @gmail.com

Project Link: [https://github.com/ayushgd/hms](https://github.com/ayushgd/repo_name)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

*Thanks to.....*
* [Bootstrap-Select](https://developer.snapappointments.com/bootstrap-select/)
* [State-City JS](https://github.com/ajayrandhawa/Indian-States-Cities-Database)
* [Choose an Open Source License](https://choosealicense.com)
* [StackOverflow](https://stackoverflow.com)



<!-- MARKDOWN LINKS & IMAGES -->
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ramvigneshb
[product-screenshot]: static/img/screenshot.png
