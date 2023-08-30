import redis from  'redis'

const client = redis.createClient();


// Create Hash using HSET
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

// Display Hash using HGETALL
client.hgetall('HolbertonSchools', (err, result) => {
	if (err) {
		console.error("Error :", err);
	} else {
		console.log("HolbertonSchools:", result);
	}
});
