# sandhya_api
An api that returns sunrise, solar noon, and sunset times for a given lat/long in the given timezone.

### Project Context
I'd love to set notifications/alarms for when sunrise, solar noon, and sunset are each day, so that I can do sandhyaavandanam at the appropriate time. I likely want them a set time prior to the atmospheric event in question. This is probably best done on my phone or in a browser app.

I figure, as a backend dev, I'd start with the API structure. I'd probably want to cache so that I don't run afoul of the generous API limitations. I'll want to deploy using AWS and then add a way to authenticate - maybe account signup, with clear delineations of what data I store and why.

I'll probably learn some Flutter to make a web and mobile app. On mobile, I can query for device permissions for GPS, Date/Time, and Notifications, and then add some controls:
* which event you want a notification for
* offset for each event
* specify address instead of using lat/long ? (depends on geocoding api limitations)
* preferred timezone (query device)

Some long-term nice-to-haves (that I probably won't get to for a very long time, if at all) are:
* Specifying a veda
* Specifying vaishnava or shaakta/shaiva
* Hindu calendar type
* Getting time based on Hindu calendar
* Adding a spot for abhivaadana details (RSi, gotra, pravara, etc), to fill in the script for you
* Using all of the above to generate a proper procedure/mantras
* Adding a step by step process to learn (screen by screen)

# Plan
### API
Run a backend in FastAPI to take requests, check a redis cache, and if nothing's there, call a lambda which then populates the cache. Should go by lat/long and date.

### Cache + Lambda
Write a lambda that takes lat/long, date, and tz (opt), and returns the sunrise, solar noon, and sunset times, in tz if specified or UTC if not.

Run a redis cache. Possibly cache times for a week in advance?

Look into https://sunrise-sunset.org/api (and add attribution where relevant). 

### Flutter? App
Create a mobile app that hooks into the OS for relevant details and creates the required notifications.

Create a web app in flutter to see what all the fuss is about, and enable browser notifications.

Provide prompts for perms, point to a good privacy policy, explain account details, attribute dependent APIs, etc.
