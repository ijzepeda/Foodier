import {
  Button,
  Group,
  Select,
  Stepper,
  TextInput,
  MultiSelect,
  Slider,
  Text,
  Input,
} from '@mantine/core';
import React, { useState } from 'react';
import { useForm } from '@mantine/form';

export default function Formpage({ setState }) {
  const [active, setActive] = useState(0);
  const nextStep = () =>
    setActive((current) => (current < 3 ? current + 1 : current));
  const prevStep = () =>
    setActive((current) => (current > 0 ? current - 1 : current));

  const form = useForm({
    initialValues: {
      daysofweek: 'whole week',
    },
  });

  const nextStepSubmit = () => {
    console.log(form.values);
    nextStep();
  };

  return (
    <div>
      <form>
        <Stepper active={active} onStepClick={setActive} breakpoint='sm'>
          <Stepper.Step label='User Information'>
            <TextInput
              label='Name'
              placeholder='Enter your name'
              {...form.getInputProps('name')}
            />
            <br />
            <TextInput
              label='Weight (in Kg)'
              type='number'
              placeholder='Enter your weight'
              {...form.getInputProps('weight')}
            />
            <br />
            <TextInput
              label='Height (in cm)'
              type='number'
              placeholder='Enter your height'
              {...form.getInputProps('height')}
            />
            <br />
            <Select
              label='Gender'
              placeholder='Select your gender'
              data={[
                { value: 'male', label: 'Male' },
                { value: 'female', label: 'Female' },
                { value: 'non-binary', label: 'Non-binary' },
                { value: 'none', label: 'Prefer not to say' },
              ]}
              {...form.getInputProps('gender')}
            />
            <br />
            <TextInput
              label='Age'
              type='number'
              placeholder='Enter your age'
              {...form.getInputProps('age')}
            />
            <br />
          </Stepper.Step>
          <Stepper.Step label='Food Preferences'>
            <TextInput
              label='Diet (e.g. vegan, vegetrian, non-vegeterian...)'
              placeholder='Enter your diet (use comma for more than one)'
              {...form.getInputProps('diet')}
            />
            <br />
            <TextInput
              label='Allergies (e.g. peanut, gluten...)'
              placeholder='Enter your allegies (use comma for more than one)'
              {...form.getInputProps('allergies')}
            />
            <br />
            <TextInput
              label='Favorite Food (e.g. sushi, porridge, haka noodles...)'
              placeholder='Enter your fav food (use comma for more than one)'
              {...form.getInputProps('favfood')}
            />
          </Stepper.Step>
          <Stepper.Step label='Meal Choices'>
            <TextInput
              label='Budget'
              placeholder='Enter your budget in CAD'
              type='number'
              {...form.getInputProps('budget')}
            />
            <br />
            <Select
              label='Days of Week'
              data={[
                { value: 'weekdays', label: 'Weekdays' },
                { value: 'weekends', label: 'Weekends' },
                { value: 'whole week', label: 'Whole Week' },
              ]}
              {...form.getInputProps('daysofweek')}
            />
            <br />
            <MultiSelect
              data={[
                { value: 'breakfast', label: 'Breakfast' },
                { value: 'lunch', label: 'Lunch' },
                { value: 'dinner', label: 'Dinner' },
              ]}
              label='Meals a day'
              placeholder='Select multiple meals'
              {...form.getInputProps('meals')}
            />
            {/* <br />
            <Input.Wrapper label='Variety'></Input.Wrapper>
            <Slider value={value} onChange={setValue} min={1} max={21} />
            <Text>{value}</Text> */}
          </Stepper.Step>

          <Stepper.Completed>Completed, Please wait.</Stepper.Completed>
        </Stepper>

        <Group position='center' mt='xl'>
          {active != 0 && active < 3 && (
            <Button variant='default' onClick={prevStep}>
              Back
            </Button>
          )}
          {active < 2 ? (
            <Button onClick={nextStep}>Next step</Button>
          ) : active == 2 ? (
            <Button onClick={nextStepSubmit}>Submit</Button>
          ) : (
            <p></p>
          )}
        </Group>
      </form>
    </div>
  );
}
