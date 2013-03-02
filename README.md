### Network Traffic Visualization

#### Built for VisualRevenue 1 March 2013 hackathon

The basic idea is to have tshark running and outputting to a file that is then
tailed. Start up the webserver and go to 127.0.0.1:8080 to view what percentage
of your traffic each protocol makes up. Dynamic refreshing is done by polling and
d3. If you want to see TCP/HTTP spike, make a get request in another browser!
