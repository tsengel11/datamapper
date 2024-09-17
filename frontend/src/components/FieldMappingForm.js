// frontend/src/components/FieldMappingForm.js

import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import axios from 'axios';
import { TextField, Button, Paper, Typography, Box, Snackbar, Alert } from '@mui/material';
import { Add as AddIcon } from '@mui/icons-material';

const FieldMappingForm = ({ onAdd }) => {
  const { register, handleSubmit, reset, formState: { errors } } = useForm();
  const [openSnackbar, setOpenSnackbar] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState('');

  const onSubmit = data => {
    axios.post('http://localhost:8000/field-mappings/', data)
      .then(response => {
        onAdd(response.data);
        reset();
        setSnackbarMessage("Mapping added successfully!");
        setOpenSnackbar(true);
      })
      .catch(error => {
        console.error("There was an error creating the mapping!", error);
        setSnackbarMessage("Failed to add mapping.");
        setOpenSnackbar(true);
      });
  };

  const handleCloseSnackbar = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }
    setOpenSnackbar(false);
  };

  return (
    <Paper elevation={3} sx={{ p: 3, mb: 4 }}>
      <Typography variant="h6" gutterBottom>
        New Field Mapping
      </Typography>
      <Box component="form" onSubmit={handleSubmit(onSubmit)} noValidate>
        <TextField
          label="API Field"
          variant="outlined"
          fullWidth
          margin="normal"
          {...register("api_field", { required: "API Field is required" })}
          error={!!errors.api_field}
          helperText={errors.api_field ? errors.api_field.message : ''}
        />
        <TextField
          label="DB Field"
          variant="outlined"
          fullWidth
          margin="normal"
          {...register("db_field", { required: "DB Field is required" })}
          error={!!errors.db_field}
          helperText={errors.db_field ? errors.db_field.message : ''}
        />
        <Button
          type="submit"
          variant="contained"
          color="primary"
          startIcon={<AddIcon />}
          sx={{ mt: 2 }}
        >
          Add Mapping
        </Button>
      </Box>
      <Snackbar
        open={openSnackbar}
        autoHideDuration={6000}
        onClose={handleCloseSnackbar}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
      >
        <Alert onClose={handleCloseSnackbar} severity={snackbarMessage.includes('successfully') ? 'success' : 'error'} sx={{ width: '100%' }}>
          {snackbarMessage}
        </Alert>
      </Snackbar>
    </Paper>
  );
};

export default FieldMappingForm;
