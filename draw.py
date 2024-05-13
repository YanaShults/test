import data
import matplotlib.pyplot as plt
import os

path_list = []


class Draw:

    def draw_plots(self, data):
        max = data['max']
        min = data['min']
        gt_corners = data['gt_corners']
        rb_corners = data['rb_corners']
        name = data['name']

        fig1 = plt.figure(figsize=(10, 8))

        plt.plot(name, max, color='red', label='Максимальные значения')
        plt.plot(name, min, color='blue', label='Минимальные значения')
        plt.xlabel('Name')
        plt.ylabel('Data')
        plt.title('Dependence of maximum and minimum values')
        plt.legend(loc='upper right')

        fig2 = plt.figure(figsize=(10, 6))

        plt.plot(name, gt_corners, color='red', label='Truth number of corners')
        plt.plot(name, rb_corners, color='blue', label='Number of corners found by the model')
        plt.xlabel('Name')
        plt.ylabel('Data')
        plt.title('Dependence of the number of corners')
        plt.legend(loc='upper right')

        if not os.path.exists('plots'):
            os.makedirs('plots')
        path_min_max = os.path.join('plots', 'max_min.png')
        fig1.savefig(path_min_max, bbox_inches='tight')
        path_list.append(path_min_max)

        path_corners = os.path.join('plots', 'corners.png')
        fig2.savefig(path_corners, bbox_inches='tight')
        path_list.append(path_corners)

        return path_list


if __name__ == "__main__":
    draw = Draw()
    paths = draw.draw_plots(data=data.data)
    print(paths)
