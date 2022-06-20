## WebMM User Requirements

### Summary

1. Written in python 3.6 (or newer)
2. Both server and client should be cross-platform.
3. No absolute paths.
4. Display comments on mouseover for the parameters.
5. Display the response in the browser
6. Compatible with Google Chrome and Firefox.
7. No size limitation on messages.
8. Simplify configuration.
9. Change the text-field colour if the limit is reached (using the "min" and "max" attributes of the XML SICD).
10. Be able to send 'out of range' messages
11. XML Validated by DTD.
12. Should be able to install on either the system being controlled, or the machine performing the controlling.
13. Compatible with legacy systems (CCS, UDP, etc.), as well as the new MQTT-based design.
14. Customise fields.
15. The controller should be able to convert between raw and human-readable units
16. Page must have a search function on list of messages as well as the values for a particular message.
17. Must be able to handle unsolicited messages (Messages that are not requested).
18. See the amount of responses you haven’t viewed yet.
19. Must show status response
20. Response must show header fields, but must also be able to hide them on user request
21. Support custom message formatting
22. Support bit fields.
23. Settings saved from previous session. Remembers old view you had.
24. Shows both the messages and their responses (Current message manager has this).
25. Log to show all the messages that are sent and received.
26. Have an option that once every second make it send. Not click send every time.
27. Documentation.
28. Multiple pipes connections.
29. Macro scripting.
30. Collapse structures.
31. Customizable data view: Abstracting the view from data.
32. Abstraction view.
33. Enter must send (default)
34. Shortcut for send (e.g ctrl+s).
25. Have Endian options (little Endian by default)
36. Tabs on message manager (single page view as Default)
37. Save payload.
38. The Command type has a "send" button (that also triggers on "Enter" when a Command message field has focus) and the Request type has a "request" button (that also triggers on "Enter" when a Request message field has focus).
39. Support alternative communication channels, such as MQTT, RS232, UDP, etc.
40. Support alternative protocols, such as NMEA or UBX.
41. Run system off-line.
42. Ability to read system database files and visualise database messages and their values.  Support for the ORT, FORT, RSR906/4, RSR210N, MSR and BR12 database formats must be included.  
43. Single DTD file.
44. Req 31: All customizable items (dials, sliders, buttons ..) and examples templates must be provided in a Toolbox format. The MMS_Toolbox must also be designed in such a way that anybody can add new items.


### Auto-generated Browser Tab

It would be quite convenient to organise the default auto-generated browser tab as follows:

On the left is a tree structure of the messages, in the structure below:

![Message Tree](MessageTree.svg)

Above (or below) the tree structure is a filter text-box (or more than one), which updates the tree live. It searches any text in the tree as well as message or module ID.

Each hierarchy node is collapsible. Ctrl+click does a open-all / close-all operation on that level. It should also be possible to mark messages as favourites, which then lists them separately, maybe below the tree in a "favourites" section.

When the user clicks on the message, the page to the right opens up all parts of that message ID. Each message type is collapsible (or hide-able). If the message has nested / embedded structures, each level is collapsible.

This view is persistent. If the user opens a different message (from the tree), and then comes back to this one later, all text boxes, check-boxes, etc. must be in the previous state.

The Command type has a "send" button (that also triggers on "Enter" when a Command message field has focus) and the Request type has a "request" button (that also triggers on "Enter" when a Request message field has focus).

The Response and Unsolicited types update automatically whenever the server pushes a message (like instant messaging - WhatsApp, etc).

It should be possible to transfer the Request-response fields to the Command fields with a click of a button (or copy and paste mechanism, but I don't think the browser has access to the system clipboard).

The Send and Request buttons can be configured (maybe with a check-box) to auto-trigger periodically.

There is no theoretical limit to the number of instances of this tab. The tree on the left can be hidden to reduce screen real-estate, and the user can undock the browser tab if multiple messages should be visible at the same time.

### Alternative Protocols

Mike mentioned something in the meeting that made me think...

It would be mighty useful to also automatically support RS232 streams such as NMEA or UBX. The XML structure already supports this, but it will break the feature where message IDs are grouped onto the same page.

One possible solution is to add a "protocol" attribute to the message definition. The same structure applies (header-payload), and you can index on part(s) of the header. In the case of NMEA, you index on a string eg. "GPGGA".

The messages are grouped by ID only when the "protocol" attribute is absent (compatible with lagacy XMLs), or the protocol is specified as "RRS MMI".

On server-side it's easy enough to support in the same way you support multiple MMI interfaces, i.e. one base class that defines the interface to the architectural layer above it, and multiple child classes; one for each protocol.

The architecture I would therefore suggest would be a polymorphism-based layered approach. Bottom-most is comms (RS232, UDP, TCP, MQTT, etc.). Above this is protocol (RRS MMI, NMEA, UBX, etc.). Above this is the XML reader and interpreter, translation to / from JSON (sent to / from the client - browser), etc. And on top is the HTTP interface to the browser, including a file reader for HTTP GET on disk resources such as *.html, *.js, *.svg, *.png, etc.

### Offline Usage

One important thing to note... It must be able to run the system off-line (i.e. not on the internet). It is mighty tempting to use [online API's](https://developers.google.com/chart/interactive/docs/gallery/gauge) that provide controls such as sliders, gauges, etc., but that won't work. All controls must be local to the server, and there may not be any online dependencies.

I have an example where I've [played around with control authoring](http://vnbitbucket:7990/projects/BR12/repos/trxc_sw/browse/WebApp). I drew the control in [InkScape](https://inkscape.org/en/) (SVG file), which I then load into the webpage DOM using JavaScript. I can then manipulate the SVG - move the slider, change the gauge position, change the text, etc. - by simple manipulation of the DOM.


