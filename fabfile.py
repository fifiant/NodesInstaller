from fabric.api import run, env, local, sudo
"""
@Author : Fawaz F. PARAISO
LICENCE : GPL
"""
# Hosts
env.hosts = ['192.168.20.200']
# Hosts Users
env.user = 'ubuntu'
#Maven settings
env.maven = "\'export PATH=${M2_HOME}/bin:${PATH}\'"
# Maven command
env.mvn = '/usr/local/maven/bin/mvn'
env.java ="\'export PATH=${JAVA_HOME}/bin:{$PATH}\'"
env.frascati = "\'export PATH=${FRASCATI_HOME}/bin:${PATH}\'"
#Credential
env.key_filename = '/home/fernand/.euca/adamcloudkey.priv'

def updateSourceListe():
    sudo('echo "deb http://archive.canonical.com/ lucid partner" >> /etc/apt/sources.list')
    run('echo "/etc/apt/source.list update successfully ..................."')

def install_java():
    sudo('apt-get update')
    sudo('apt-get install sun-java6-jre sun-java6-bin sun-java6-jdk sun-java6-plugin sun-java6-fonts')
    sudo('echo "export JAVA_HOME=\'/usr/lib/jvm/java-6-sun-1.6.0.24/jre\'" >> ~/.bashrc')
    sudo('echo %(java)s >> ~/.bashrc' %env)
    run('echo "Java Installation finished successfully............"')

def install():
    updateSourceListe()
    #install_java()
    install_maven()
    install_frascati()

def install_maven():
    run('echo "download Maven" ')
    run('wget http://mirror.ibcp.fr/pub/apache//maven/binaries/apache-maven-2.2.1-bin.tar.gz;')
    run('mkdir -p ~/install;')
    run('mv apache-maven-2.2.1-bin.tar.gz ~/install;')
    run('cd ~/install && tar -xzvf apache-maven-2.2.1-bin.tar.gz;')
    sudo(' cd ~/install && mv apache-maven-2.2.1 /usr/local/maven')
    sudo('echo "export M2_HOME=\'/usr/local/maven/\'" >> ~/.bashrc')
    sudo('echo %(maven)s >> ~/.bashrc' %env)
    sudo('. .bashrc')
    run('%(mvn)s -v'%env)


def install_frascati():
    sudo('aptitude install -y unzip')
    run('echo "download FraSCAti" ')
    run('wget http://download.forge.objectweb.org/frascati/frascati-1.4-bin.zip;')
    run('mkdir -p ~/install;')
    run('mv frascati-1.4-bin.zip ~/install;')
    run('cd ~/install && unzip frascati-1.4-bin.zip ;')
    sudo('echo "export FRASCATI_HOME=\'~/install/frascati-runtime-1.4\'" >> ~/.bashrc')
    sudo('echo %(frascati)s >> ~/.bashrc' %env)
    sudo('. .bashrc')

def uptime():
    run('uptime')

def host_info():
    print 'Checking lsb_release of host: ',  env.host
    run('lsb_release -a ')
