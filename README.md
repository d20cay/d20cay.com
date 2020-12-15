# d20cay.com

This repository contains the code for the d20cay.com domain.

Version: 2020.51.1

## Current structure:  
Homepage  
\-  Clip Studio Paint Cheatsheet  
\-  Linux Cheatsheet  
\-  School Cheatsheets  

\-  Minecraft Servers  
\-  Minecraft Cheatsheet
\-  Hypixel Player Stats

\- ae  
\- oe  
\- ue  
\- Umlaut  
\- Cryptography

\- Contact

\- Changelog

## d20cay Development and Deployment

## Webserver

1. Open terminal
2. cd into this directory
3. Install all npm deps with `npm install`
4. Run it in dev mode with `npm run dev` OR
5. Export it to a static website with `npm run export` OR
6. Build it with `npm run build` and launch the prod version with `node __sapper__/build`

## Proxy Api

Run `uvicorn main:app --host localhost` from the folder the main.py file resides in. Add `--reload` if in dev mode.
