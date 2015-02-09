Basic form + Python cgi script
------------------------------

### Apache Setup

Enable cgi module

```
a2enmod cgi
```

Configure behaviour of cgi module

```
<Directory /mnt/data1/git/web-sandbox/form_upload>
    Require all granted
</Directory>
	
<Directory /mnt/data1/git/web-sandbox/form_upload/cgi-bin>
    Options +ExecCGI
    SetEnv MANTID_MD5_DATA_STORE /mnt/data1/ExternalData/uploaded/MD5
    AddHandler cgi-script .py
    Require all granted
</Directory>

ScriptAlias /cgi-bin/ "/mnt/data1/git/web-sandbox/form_upload/cgi-bin/"
```
