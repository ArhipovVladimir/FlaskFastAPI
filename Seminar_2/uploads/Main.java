public class Main {
    public static void main(String[] args) {
        String[][] data;
        data = new String[][]
                {{"11", "1", "3", "8"},
                        {"1", "1", "2", "2"},
                        {"1", "1", "2", "3"},
                        {"2", "1", "5", "1"}};
        int res = 0;
        try {
            res = calcManrix(data);
        } catch (MyArraySizeException e) {
            e.printStackTrace();
        } catch (MyArrayDataException e) {
            e.printStackTrace();
        }
        System.out.println(res);

    }

    private static int calcManrix(String[][] matrix) throws MyArraySizeException, MyArrayDataException {
        if (matrix.length != 4) {
            throw new MyArraySizeException("Не верный размер массива");
        } else if (matrix[1].length != 4) {
            throw new MyArraySizeException("Не верный размер массива");
        } else if (matrix[2].length != 4) {
            throw new MyArraySizeException("Не верный размер массива");
        } else if (matrix[3].length != 4) {
            throw new MyArraySizeException("Не верный размер массива");
        }

        int val = 0;
        int sum = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                try {
                    val = Integer.parseInt(matrix[i][j]);
                } catch (NumberFormatException e) {
                    throw new MyArrayDataException(i, j);
                }

                sum += val;
            }
        }
        return sum;
    }

}


