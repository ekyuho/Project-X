module.exports = {
  apps : [
      {
        name: "playbook",
        script: "./playbook.py",
        watch: true,
        env: {
          "PATH": "/home/ubuntu/p3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        }
      }
  ]
}
