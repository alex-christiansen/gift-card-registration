<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/alex-christiansen/gift-card-registration">
    <img src="images/automation-icon.png" alt="Logo" width="80" height="80">
  </a>
  

<h3 align="center">Automated Gift Card Registration</h3>

  <p align="center">
    This script helps automate the registration of gift cards on <a href="https://redeem.giftcards.com/">https://redeem.giftcards.com/</a> including capturing the resulting gift card number and pin after registration.
    <br />
    <a href="https://github.com/alex-christiansen/gift-card-registration"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/alex-christiansen/gift-card-registration">View Demo</a>
    ·
    <a href="https://github.com/alex-christiansen/gift-card-registration/issues">Report Bug</a>
    ·
    <a href="https://github.com/alex-christiansen/gift-card-registration/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://redeem.giftcards.com/)

When certain gift cards are purchased, you must redeem them for a specific store. After redeeming them, you receive a new gift card number and pin for that specific store (and dollar value). The script will read inputted gift card numbers from a google sheet, register them through the website and then paste the resulting gift card number and pin in the google sheet. 

Using the python package <a href="https://pypi.org/project/selenium/">Selenium</a>, we can automate this process. All you need to do is upload the original gift card numbers and pins and the script does the rest.
<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Selenium](https://pypi.org/project/selenium/)
* [Chrome Webdriver](https://chromedriver.chromium.org/downloads)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

There are several steps before you can get up and running but once completed, running the script is easy

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* [Homebrew](https://www.freecodecamp.org/news/python-version-on-mac-update/#:~:text=How%20to%20Install%20Homebrew%20on%20Mac)

  ```sh
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```

* Python 3

  ```sh
  brew install python
  ```

    ```sh
  python --version
  ```

* [Chrome Driver](https://chromedriver.chromium.org/downloads)

* Service Account for Google Console
https://console.cloud.google.com/
API & Services
Google Sheets
Google Drive


### Installation

1. Get a free SA Key at [https://example.com](https://example.com)
2. Create google sheet (https://docs.google.com/spreadsheets/d/1PqV52zh53bcpRZsde9E6uRnDqG08CHBgi4SOgKW1_AY/copy)
3. Share SA with Google Sheet
2. Clone the repo
   ```sh
   git clone https://github.com/alex-christiansen/gift-card-registration.git
   ```
3. Install packages
   ```pip3 install -r python/requirements.txt
   ```
4. Update file names
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/alex-christiansen/gift-card-registration/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/alex-christiansen/gift-card-registration](https://github.com/alex-christiansen/gift-card-registration)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/alex-christiansen/gift-card-registration.svg?style=for-the-badge
[contributors-url]: https://github.com/alex-christiansen/gift-card-registration/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/alex-christiansen/gift-card-registration.svg?style=for-the-badge
[forks-url]: https://github.com/alex-christiansen/gift-card-registration/network/members
[stars-shield]: https://img.shields.io/github/stars/alex-christiansen/gift-card-registration.svg?style=for-the-badge
[stars-url]: https://github.com/alex-christiansen/gift-card-registration/stargazers
[issues-shield]: https://img.shields.io/github/issues/alex-christiansen/gift-card-registration.svg?style=for-the-badge
[issues-url]: https://github.com/alex-christiansen/gift-card-registration/issues
[license-shield]: https://img.shields.io/github/license/alex-christiansen/gift-card-registration.svg?style=for-the-badge
[license-url]: https://github.com/alex-christiansen/gift-card-registration/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/christiansenalex
[product-screenshot]: images/giftcards.com.png
