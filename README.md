Section 1: Purpose
RC Event Announce is an open-source application released under GNU Public License to help distribute information about upcoming events. It’s primary stakeholders are 1) BMRCs, who can use the app to easily maintain a calendar of upcoming events in their region, 2) Event planners/promoters, who can use the application to reach their target market, 3) the BM community, who can use the app for their region to find events in their area. 


Section 2: High Level Entities
Events: Events can be created by event planners and reviewed by an RC or created by an RC. They will remain in the database for 30 days after the event. Events are tagged to categorize them for their intended audience. 

RC view: RCs can ensure that an event is relevant to the burner community before it is visible to participants.

Distribution: After RC approval, the event will be visible on a public facing Google Calendar page and sent to a distribution email list. 

Section 3: Low Level Design
Event object: Database entry for each event. Date/Time, Location, Ticket price/availability, Presale link, Website/Contact info

Event app: Creates Event objects. Scrapes Facebook (and other websites?) for event information to populate fields. Flushes database of entries 30 days after the event. 

RC View app: Allows event management and approval for distribution.

Participant View app:Allows participants to manage their email address and subscribe/unsubscribe to different audiences

Distribution App: Interfaces with Google Calendar to maintain calendar. Interfaces with Google Mail to distribute email list to participants depending on their stated interests.
