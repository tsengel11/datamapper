// frontend/src/App.js

import React, { useContext } from 'react';
import { Container, Grid, Typography, AppBar, Toolbar, IconButton } from '@mui/material';
import { Brightness4, Brightness7 } from '@mui/icons-material';
import { useTheme } from '@mui/material/styles';
import { ColorModeContext } from './index';
import FieldMappingForm from './components/FieldMappingForm';
import FieldMappingList from './components/FieldMappingList';
import SchedulerControl from './components/SchedulerControl';
import WebhookHandler from './components/WebhookHandler';

function App() {
  const theme = useTheme();
  const colorMode = useContext(ColorModeContext);

  return (
    <div>
      <AppBar position="static" color="primary">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            DataMapper
          </Typography>
          <IconButton color="inherit" onClick={colorMode.toggleColorMode}>
            {theme.palette.mode === 'dark' ? <Brightness7 /> : <Brightness4 />}
          </IconButton>
        </Toolbar>
      </AppBar>
      <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
        <Grid container spacing={4}>
          <Grid item xs={12} md={6}>
            <FieldMappingForm />
            <FieldMappingList />
          </Grid>
          <Grid item xs={12} md={6}>
            <SchedulerControl />
            <WebhookHandler />
          </Grid>
        </Grid>
      </Container>
    </div>
  );
}

export default App;
