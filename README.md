# CS 326 Group 12

## Team Members

- [Matt Rossman](team/matt-rossman.md)
- [Ayush Khandelwal](team/AyushKhandelwal.md) 
- [Alexandra Ferrucci](team/ali-ferrucci.md)
- [Wesley Tey](team/wtey.md)

## Overview

We are building a news app with a focus on users' mental health that allows more control over the type of content consumed.
Users will be able to filter out negative articles from various sources. They can also filter out certain topics that upset them. We are considering showing stats about the article's trustworthiness as well.
This makes readers less vulnerable to emotional-manipulation tactics, or simply lets them see the world in a more positive light.

## Topic Requirements

- Ajax - for interfacing with the news and sentiment APIs
- Mobile - since most news consumption is on mobile devices

## Running

The frontend and backend can be run with Docker Compose. First, set up your API keys in the config.yaml file as specified in the [API's README](api/README.md). Then start the api and website services with:

    docker-compose up

This will publish the API on port 5001 and the website on port 5000. Thus, you can access the site at http://localhost:5000

Note that the weather API calls will be blocked by the browser causing the page not to fully load, which can be circumvented through [this Chrome extension](https://chrome.google.com/webstore/detail/moesif-orign-cors-changer/digfbfaphojjndkpccljibejjbppifbc?hl=en-US).