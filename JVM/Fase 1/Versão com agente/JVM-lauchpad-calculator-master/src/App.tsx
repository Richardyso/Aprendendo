import { useState } from 'react'
import './App.css'

const INITIAL_VALUE = '0'
const ERROR_MESSAGE = 'Erro'
const OPERATORS = ['+', '-', '*', '/', '%']
const FUNCTION_BUTTONS = ['C', '⌫']
const EQUALS_BUTTON = '='
const ZERO_BUTTON = '0'

const CALCULATOR_BUTTONS = [
  'C', '⌫', '%', '/',
  '7', '8', '9', '*',
  '4', '5', '6', '-',
  '1', '2', '3', '+',
  '0', '.', '='
]

type ButtonType = 'number' | 'operator' | 'function' | 'equals'

function getButtonType(button: string): ButtonType {
  if (button === EQUALS_BUTTON) return 'equals'
  if (OPERATORS.includes(button)) return 'operator'
  if (FUNCTION_BUTTONS.includes(button)) return 'function'
  return 'number'
}

function getButtonClassName(button: string): string {
  const baseClass = 'btn'
  const typeClass = `btn-${getButtonType(button)}`
  const zeroClass = button === ZERO_BUTTON ? 'btn-zero' : ''
  
  return `${baseClass} ${typeClass} ${zeroClass}`.trim()
}

function useCalculator() {
  const [display, setDisplay] = useState(INITIAL_VALUE)

  const appendToDisplay = (value: string) => {
    const isDisplayEmpty = display === INITIAL_VALUE
    const isNotDecimalPoint = value !== '.'
    
    if (isDisplayEmpty && isNotDecimalPoint) {
      setDisplay(value)
    } else {
      setDisplay(display + value)
    }
  }

  const clearDisplay = () => {
    setDisplay(INITIAL_VALUE)
  }

  const deleteLastCharacter = () => {
    const hasOnlyOneCharacter = display.length === 1
    
    if (hasOnlyOneCharacter) {
      setDisplay(INITIAL_VALUE)
    } else {
      setDisplay(display.slice(0, -1))
    }
  }

  const calculateResult = () => {
    try {
      const result = eval(display)
      setDisplay(String(result))
    } catch {
      setDisplay(ERROR_MESSAGE)
    }
  }

  const handleButtonPress = (button: string) => {
    const actions: Record<string, () => void> = {
      'C': clearDisplay,
      '⌫': deleteLastCharacter,
      '=': calculateResult
    }

    const action = actions[button]
    
    if (action) {
      action()
    } else {
      appendToDisplay(button)
    }
  }

  return {
    display,
    handleButtonPress
  }
}

function App() {
  const { display, handleButtonPress } = useCalculator()

  return (
    <div className="calculator">
      <Display value={display} />
      <Keyboard 
        buttons={CALCULATOR_BUTTONS} 
        onButtonPress={handleButtonPress} 
      />
    </div>
  )
}

function Display({ value }: { value: string }) {
  return (
    <div className="display">
      <span className="display-text">{value}</span>
    </div>
  )
}

function Keyboard({ 
  buttons, 
  onButtonPress 
}: { 
  buttons: string[]
  onButtonPress: (button: string) => void 
}) {
  return (
    <div className="keyboard">
      {buttons.map((button, index) => (
        <button
          key={index}
          className={getButtonClassName(button)}
          onClick={() => onButtonPress(button)}
        >
          {button}
        </button>
      ))}
    </div>
  )
}

export default App
