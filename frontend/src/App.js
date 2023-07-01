import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import {
  Stepper,
  Button,
  Group,
  Center,
  Container,
  createStyles,
  Title,
  rem,
  Header,
} from '@mantine/core';
import Formpage from './formPage';

const useStyles = createStyles((theme) => ({
  wrapper: {
    paddingTop: `calc(${theme.spacing.xl} * 2)`,
    minHeight: '100vh',
    width: '100%',
    backgroundColor: `#5765F200`,
    // backgroundRepeat: 'no-repeat',
    // backgroundPosition: 'top left',
    position: 'relative',
    color: theme.black,
  },

  title: {
    color: theme.white,
    fontSize: 52,
    fontFamily: `Greycliff CF, ${theme.fontFamily}`,
    marginBottom: `calc(${theme.spacing.xl} * 1.5)`,
  },
}));

function App() {
  const [mainState, setMainState] = useState({});
  const { classes } = useStyles();

  useEffect(() => {
    console.log(mainState);
  }, mainState);
  return (
    <div className='App'>
      <Header
        height={56}
        style={{
          backgroundColor: '#5765F2',
        }}
      >
        <Center
          style={{
            color: 'white',
            fontSize: '32px',
            fontWeight: 'bolder',
            alignItems: 'center',
          }}
        >
          Foodier
        </Center>
      </Header>
      <div className={classes.wrapper}>
        <Container
          size='sm'
          style={{
            backgroundColor: 'white',
            padding: '2%',
            borderRadius: '5px 5px',
            boxShadow: '0px 0px 5px #dddddd',
          }}
        >
          <Formpage setState={setMainState} />
        </Container>
      </div>
    </div>
  );
}

export default App;
