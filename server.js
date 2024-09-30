// server.js
const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Endpoint to handle form submission
app.post('/send-email', (req, res) => {
    const { fullname, email, message } = req.body;

    // Create a transporter for sending emails
    const transporter = nodemailer.createTransport({
        service: 'gmail', // Use your email provider
        auth: {
            user: 'samaranjanedu01@gmail.com',
            pass: 'M#manjhi312', // Use environment variables for security
        },
    });

    const mailOptions = {
        from: email,
        to: 'recipient-email@example.com',
        subject: `New message from ${fullname}`,
        text: message,
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            return res.status(500).json({ status: 'error', message: error.toString() });
        }
        res.status(200).json({ status: 'success' });
    });
});

// Start the server
app.listen(3000, () => {
    console.log('Server is running on port 3000');
});

