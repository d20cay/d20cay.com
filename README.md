# d20cay.com

This repository contains the code for the d20cay.com domain.

Version: 2021.51.2

## Current structure:

- Project
  - Cryptography
  - Pi
  - Prime Factorization
  - Secret Santa
  - Umlaut
  - YouTube Music Library Analysis
- Minecraft
  - Commands
  - Server
  - Hypixel Bedwars Statistics
- Cheatsheets
  - Ascii
  - Clip Studio Paint  
  - Linux Cheatsheet  
  - School Cheatsheets

- ae  
- oe  
- ue

- Contact

- Changelog
- Imprint
- Privacy

## d20cay Development and Deployment

## Webserver

1. Open terminal
2. cd into this directory
3. Install all npm deps with `npm install`
4. Run it in dev mode with `npm run dev` OR
5. Export it to a static website with `npm run export` OR
6. Build it with `npm run build` and launch the prod version with `node build`

## Proxy Api

Run `uvicorn main:app --host localhost` from the folder the main.py file resides in. Add `--reload` if in dev mode.
If `uvicorn` isn't installed properly you might need to start it
with `python -m uvicorn main:app --host localhost --reload`.
