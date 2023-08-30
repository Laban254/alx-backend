import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Handle successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection error
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});


function setNewSchool(schoolName, value) {
	client.set(schoolName, value, (err, reply) => {
		if(err) {
			console.log("error setting school :", err);
		} else {
			console.log("school set :",  reply)
		}
	});
}

function displaySchoolValue(schoolName) {
	client.get(schoolName, (err, reply) => {
		if (err) {
			console.log("error retrieving school :",  err);
		} else {
			console.log("school retrieved :", reply);
		}
	});
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
