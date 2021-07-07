# Kubernetes_webui
#### Steps to follow-
1. Set up Kubernetes cluster over cloud. In the master node, set up the webserver using httpd.
2. Download all the files in your server.
3. Download httpd software in rhel using $yum install httpd -y
4. Save cgi-doc.py in /var/www/cgi-bin folder of httpd and save the remaining in /var/www/html. cgi-doc.py is our backend file and remaining are the frontend files.
5. Use your instance's ip address in script part of kub.html file (instead of ip already present).
6. Make cgi-doc.py file executable using $chmod 755 cgi-doc.py
7. Grant permission to apache group to execute commands in the server OS. Edit the file /etc/sudoers and add "apache ALL=(ALL) NOPASSWD:ALL" in line no 101 and save using :wq!
8. Start the httpd services using "$systemctl start httpd" .It can be made permanent using "$systemctl enable httpd" command
9. To disable selinux temporarily and stop the firewall, use the command "$setenforce 0" and "$systemctl stop firewalld" resp.
10. Make sure to add the inbound rule in this security group of the instance to allow http on port 80
11. Now check the connectivity from the browser using the url format-"<protocol>//<ip>:<port>/kub.html" EG- http://192.168.2.18/index.html
  
  
Note- Make sure you kubernetes cluster is configured and running before making the webportal for the same. In case the cluster is not running, use documents to set it up.
  
