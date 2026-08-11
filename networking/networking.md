
Imagine You Open https://google.com

What happens?

You
 ↓
DNS finds Google's IP
 ↓
Connect to Google's server using HTTPS (port 443)
 ↓
TCP establishes a reliable connection
 ↓
Server sends the webpage back
 ↓
Browser displays Google

Everything we'll learn fits into this flow.

1. IP Address
What is it?

An IP address is the unique address of a device on a network.

Think of it like a house address.

Example:

House Address:
10 Park Street

IP Address:
192.168.1.10

Without an address, nobody knows where to send data.

Examples:

192.168.1.10
172.16.0.1
8.8.8.8

Your laptop has an IP.

Google's server has an IP.

Every device connected to a network has an IP.

Practice

See your IP:

ip addr

or

hostname -I
2. DNS (Domain Name System)

Imagine if every website had to be remembered like this:

142.250.190.78

instead of

google.com

That would be difficult.

DNS is like the contacts list in your phone.

Instead of remembering:

+91xxxxxxxxxx

you remember:

Mom

Similarly,

google.com

is translated into an IP address by DNS.

Real Example

You type:

google.com

DNS replies:

142.250.xxx.xxx

Now your computer knows where to connect.

3. Port

A device can run many services at once.

Imagine an apartment building.

Building Address
↓

Apartment 101
Apartment 102
Apartment 103

The IP address is the building.

The port is the apartment number.

Example:

IP:
192.168.1.10

Port:
22
80
443
3306

Same computer.

Different services.

Common Ports
Port	Service
22	SSH
80	HTTP
443	HTTPS
3306	MySQL
5432	PostgreSQL

You don't need to memorize all of them, but 22, 80, and 443 are used constantly in DevOps.

4. TCP

Suppose you send your friend a 500-page book.

You want every page to arrive in order.

TCP works like this.

It:

Sends data in pieces.
Checks every piece arrives.
Resends missing pieces.
Reassembles everything in order.

Reliable, but a bit slower.

Used by:

Websites
SSH
Email
File downloads
5. UDP

Now imagine you're watching a live cricket match.

If one video frame is lost, you don't want the whole stream to stop while waiting for it.

You'd rather continue watching.

That's UDP.

It:

Sends data quickly.
Doesn't check if everything arrives.
Doesn't resend lost packets.

Used by:

Video streaming
Voice calls
Online games
TCP vs UDP
TCP	UDP
Reliable	Fast
Checks delivery	Doesn't check
Resends lost data	Doesn't resend
Used for websites	Used for streaming
6. HTTP

HTTP stands for HyperText Transfer Protocol.

It's the language your browser and a web server use to communicate.

When you open:

http://example.com

your browser sends a request.

The server responds with HTML, CSS, JavaScript, images, and more.

By default, HTTP uses port 80.

7. HTTPS

HTTPS is simply HTTP with encryption.

Imagine sending a postcard.

Anyone who handles it can read it.

That's like HTTP.

Now imagine putting the message inside a locked envelope.

Only the intended recipient can open it.

That's HTTPS.

It uses TLS/SSL encryption and typically runs on port 443.

When you see:

https://

your connection is encrypted.

8. SSH

SSH stands for Secure Shell.

It lets you securely log in to another computer.

Example:

ssh user@192.168.1.10

or

ssh ubuntu@ec2-xx-xx-xx.compute.amazonaws.com

As a DevOps engineer, you'll use SSH to:

Connect to Linux servers.
Deploy applications.
Manage cloud virtual machines.
Troubleshoot remote systems.

By default, SSH uses port 22.
