module.exports = {
    apps:[
        {
            name:'python-api',
            script:'./server.py',
            args:[""],
            exec_mode: 'fork',
            autorestart:true,
            max_restart: 5,
            interpreter: "pipenv",
            interpreter_args: "run python3" 
        }
    ]
}