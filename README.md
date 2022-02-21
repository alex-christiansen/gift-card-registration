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
**Disclaimer: This project was built for fun. Use this at your own risk. I make no promises to fix bugs or update in the future. The script is currently built to handle only $500 gift cards.**

When certain gift cards are purchased, you must redeem them for a specific store. After redeeming them, you receive a new gift card number and pin for that specific store (and dollar value). The script will read inputted gift card numbers from a Google Sheets, register them through the website and then paste the resulting gift card number and pin in the Google Sheets.

Using the python package <a href="https://pypi.org/project/selenium/">Selenium</a>, we can automate this process. All you need to do is upload the original gift card numbers and pins and the script does the rest.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Selenium](https://pypi.org/project/selenium/)
* [Chrome Webdriver](https://chromedriver.chromium.org/downloads)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get started, you'll need to install Python3 and  Chrome Webdriver. In addition, you'll need to create a free GCP account so that you can use an API to access the gift card numbers stored in a Google Sheet.

### Prerequisites

* Install [Homebrew](https://www.freecodecamp.org/news/python-version-on-mac-update/#:~:text=How%20to%20Install%20Homebrew%20on%20Mac). Homebrew is a free and open-source software package management system that simplifies the installation of software on Apple's operating system, macOS. We'll use it to install Python. To install Homebrew, run the following commands in the terminal:

  ```sh
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```

* Install Python 3. Now that Homebrew is installed, we can run the below to install Python:

  ```sh
  brew install python
  ```
  
  Make sure that you have the right version installed, run:

  ```sh
  python --version
  ```

  The output should look like `Python 3.9.9` (your version may vary).

* Install [Chrome Driver](https://chromedriver.chromium.org/downloads). Chrome Driver is used in conjunction with Selenium to manupulate your browser. Make sure to download the correct Chrome version. This was built using version 97. You can see what version you are running by going to `Settings -> About Chrome` in Chrome.

* Sign up for a free Google Cloud account (<https://console.cloud.google.com/>). You'll need to this to create a service account so that the program can access the data in Google Sheets.

### Installation

#### Create a Google Sheet

1. Create a Google Sheet (<https://docs.google.com/spreadsheets/d/1PqV52zh53bcpRZsde9E6uRnDqG08CHBgi4SOgKW1_AY/copy>) using this exact template. Note: The data MUST reside in the first sheet in the workbook (if for some reason you have multiple tabs). You can name the sheet whatever you want.

2. DO NOT change the order of the columns.

3. Fill out columns A-G + I. If you don't fill out one of the required columns the program won't run. Be sure to fill out the amount otherwise it won't be able to complete the order.

#### Enable Google APIs and Create Service Account

1. Enable the Google Drive and Google Sheets API by going to the menu bar inside of the Google Cloud console and select APIs & Services then [Library](https://console.cloud.google.com/apis/library).

2. Search for `Google Drive API` and make sure it's enabled. If not, simply click enable. Repeat for the `Google Sheets API`.

3. Create a service account by going to APIs & Services then [Credentials](https://console.cloud.google.com/apis/credentials). At the top select `+Create Credential` then `Service Account`.

4. Give the service account any name (e.g. gift-card-automation), click `Create and Continue` then `Done`. You DO NOT need to do steps two and three.

5. Back on the [credentials](https://console.cloud.google.com/apis/credentials) page, grab the email for your service account.

6. Share the Google Sheet that you created above with this service account and make sure it has edit access.

#### Clone the Repo & Install Packages

1. Clone this repo onto your local machine. For those unfamilar with this process, you'll generally want to clone it to your desktop. To do that, open up Terminal and type `cd ~/Desktop`. Then you can run the below:

  ```sh
  gh repo clone alex-christiansen/gift-card-registration
  ```

2. Change your working directory to gift-card-registration. If you saved the repo to your Desktop, you can do this with the below

  ```sh
  cd ~/Desktop/gift-card-registration
  ```

3. Install packages

  ```sh
  pip3 install -r python/requirements.txt
  ```

#### Create JSON Key 

1. Create a JSON key for your service account.
  
* Go back to the service account in the console, `APIs & Services -> Credentials`.
* Click on the service account name that you created before
* At the top, click `Keys` -> `Add Key`
* Pick `JSON` and then create the keys
* A file will get downloaded to your computer that you'll need to move to this directory

2. Rename the JSON key to `google-api.json` (just find it in your downloads and rename).

3. Move the JSON key to this directory by running the below (you may have to change the directory names)

   ```sh
   mv ~/Downloads/google-api.json ~/Desktop/gift-card-registration/
   ```

#### Rename program variables

1. Update `chromedriver_location = "filepath/chromedriver"`

* Update the location of chromedriver, if you just downloaded it, the path will be something like `/Users/username/Downloads/chromedriver`
* Make sure chromedriver can run by double-clicking it (I've assumed you already unzipped it)
* If you can't, go to `System Preferences` -> `Security & Privacy` and make sure the program has permissions to run

2. Update `sheet = client.open('google-drive-file-name')` with the correct sheet name. Change `google-drive-file-name` to the name of your Google Sheet that has the data.

<!-- USAGE EXAMPLES -->
## Usage

After everything has been installed, you can run the script by typing

```sh
python3 ~/Desktop/gift-card-registration/python/web_automation.py
```

Note: If you try to use other browsers while the script is running it will error out. If it errors out for any reason, just close the browser it was in and run it again. 

<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<!-- <p align="right">(<a href="#top">back to top</a>)</p> -->

<!-- ROADMAP -->
## Roadmap

* [ ] Feature 1
* [ ] Feature 2
* [ ] Feature 3
  * [ ] Nested Feature

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

<!-- Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com -->

Project Link: [https://github.com/alex-christiansen/gift-card-registration](https://github.com/alex-christiansen/gift-card-registration)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

* []()
* []()
* []() -->

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
