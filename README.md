# zabbix-gearman-template
##Gearman monitoring template with task autodiscovery, for zabbix 3.0

### Zabbix server
1. pip install gearman
2. Put check_gearman.py in your external scripts directory
3. Make it executable (chmod +x ...)

### Zabbix frontend
4. Import zbx_gearman_template.xml
5. Link it with desired hosts
6. Set {$GEARMANPORT} macro if port is different than default 4730
