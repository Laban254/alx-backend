import redis from 'redis';
import util from 'util';
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


// Promisify the client.get function
const getAsync = util.promisify(client.get).bind(client);

// Async function to display school value
async function displaySchoolValue(schoolName) {
    try {
        const reply = await getAsync(schoolName);
        console.log("school retrieved :", reply);
    } catch (err) {
        console.log("error retrieving school:", err);
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
