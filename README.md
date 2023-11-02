# Crypto Data API Pull

A Python script for fetching cryptocurrency data from the CoinMarketCap API and storing it in a CSV file for analysis. This script pulls the latest cryptocurrency listings and goes ahead to make a sample visualisation.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Data Storage](#data-storage)
- [Data Visualisation](#data-visualisation)
- [Contributing](#contributing)


## Introduction

The "Crypto Data API Pull" script is designed to retrieve data from the CoinMarketCap API and store it for further analysis. It fetches the latest cryptocurrency listings, and plots a sample visual using Seaborn.

## Features

- Fetches the latest cryptocurrency data from the CoinMarketCap API.
- Stores the data in a CSV file with a timestamp for historical tracking.
- Visualizes data with Seaborn plots.

## Getting Started

### Prerequisites

Before running the script, you need to install the required Python packages. You can do this using pip:

```bash
pip install requests pandas seaborn matplotlib
```

### Installation
- Clone this repository to your local machine:
- Modify the `X-CMC_PRO_API_KEY` value in the script with your own coinmarketcap API key
-Run the scripts

## Usage
The script can be used to fetch cryptocurrency data and perform various analyses. You can modify the script to fetch data for different cryptocurrencies and perform various forms of analyses

## Data Storage
The script stores the fetched data in a CSV file. If the file does not exist, it creates one with headers. If the file already exists, new data is appended to it without recreating headers.

## Data Visualisation
This script performs a sample visualisation of the volume of price changes on various types of cryptocurrencies over different time intervals.

## Contributing
If you'd like to contribute to this project, please follow these steps:

Fork the repository on GitHub.
Create a new branch with a descriptive name for your feature or bug fix.
Make your changes and commit them to your branch.
Push your changes to your fork on GitHub.
Create a pull request from your branch to the main repository.
