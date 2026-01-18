let n = parseInt(8);

if (n > 10) {
	console.log("Inválido. Insira um número de 1 a 10 !");
} else {
	for (i = 1; i <= 10; i++) {
		console.log(`${i} x ${n} = ${i * n}`);
	};
};