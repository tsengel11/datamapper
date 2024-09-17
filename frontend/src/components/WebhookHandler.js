// frontend/src/components/WebhookHandler.js

import React, { useState } from 'react';
import axios from 'axios';
import { TextField, Button, Paper, Typography, Box, Alert } from '@mui/material';
import { Send as SendIcon } from '@mui/icons-material';

const WebhookHandler = () => {
  const [payload, setPayload] = useState('{"event": "test"}');
  const [responseMessage, setResponseMessage] = useState(null);
  const [errorMessage, setErrorMessage] = useState(null);

  const sendWebhook = () => {
    try {
      const data = JSON.parse(payload);
      axios.post('http://localhost:8000/webhook/', data)
        .then(response => {
          setResponseMessage("Webhook sent successfully!");
          setErrorMessage(null);
        })
        .catch(error => {
          console.error("Error sending webhook:", error);
          setErrorMessage("Failed to send webhook.");
          setResponseMessage(null);
        });
    } catch (error) {
      setErrorMessage("Invalid JSON format.");
      setResponseMessage(null);
    }
  };

  return (
    <Paper elevation={3} sx={{ p: 3 }}>
      <Typography variant="h6" gutterBottom>
        Send Webhook
      </Typography>
      <Box component="div" sx={{ mb: 2 }}>
        <TextField
          label="Webhook Payload (JSON)"
          variant="outlined"
          fullWidth
          multiline
          minRows={4}
          value={payload}
          onChange={(e) => setPayload(e.target.value)}
          error={!!errorMessage}
          helperText={errorMessage}
        />
      </Box>
      <Button
        variant="contained"
        color="secondary"
        startIcon={<SendIcon />}
        onClick={sendWebhook}
      >
        Send Webhook
      </Button>
      {responseMessage && (
        <Alert severity="success" sx={{ mt: 2 }}>
          {responseMessage}
        </Alert>
      )}
      {errorMessage && (
        <Alert severity="error" sx={{ mt: 2 }}>
          {errorMessage}
        </Alert>
      )}
    </Paper>
  );
};

export default WebhookHandler;
